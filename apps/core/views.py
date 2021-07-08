from django.shortcuts import render, redirect
import pygal
import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.core.models import Gitstats
from apps.core.forms import AddGitstatsForm


def git_repo_home(request):
   

    git_repos = Gitstats.objects.all().select_related('creator_user')

    context = {
        'all_git_repos': git_repos,
    }
    return render(request, 'pages/home.html', context)

@login_required
def git_repo_create(request):
    if request.method == 'POST':
       
        form = AddGitstatsForm(request.POST)
        if form.is_valid():
          
            logged_in_user = request.user
            

            Gitstats.objects.create(
                user_name=form.cleaned_data['user_name'],
                git_profile=form.cleaned_data['git_profile'],
                panel_type=form.cleaned_data['panel_type'],
                git_profile_description = form.cleaned_data['git_profile_description'],
                creator_user=logged_in_user,
            )
            return redirect('/')
    else:
       
        form = AddGitstatsForm()
    context = {
        'form': form,
    }
    return render(request, 'pages/save_form.html', context)


def git_dashboard(request, git_id):
  
    git_repo_requested = Gitstats.objects.get(id=git_id)
  
   
    context = {
        'git_repo': git_repo_requested,
        
    }
    
    username = git_repo_requested.git_profile.split('/')[-1]
    
     
    response = requests.get(f'https://api.github.com/users/{username}/repos')
    repo_data = response.json()
    

    if git_repo_requested.panel_type == "Treemap":
        treemap_chart = pygal.Treemap()
        treemap_chart.title = 'Size of my Github Repositories'
        for item in repo_data:
            treemap_chart.add(item['name'], int(item['size']))

    
        context = {
            'chart' : treemap_chart.render_data_uri(),
            'title' : "Github Repo Size",
        }   
    
    elif git_repo_requested.panel_type == "Pie":
        pie_chart = pygal.Pie()
        pie_chart.title = 'Size of my Github Repositories'
        for item in repo_data:
            pie_chart.add(item['name'], int(item['size']))

    
        context = {
            'chart' : pie_chart.render_data_uri(),
            'title' : "Github Repo Size",
        }
    
    else:
        bars = pygal.HorizontalBar(logarithmic=True)
        bars.title = 'Size of my Github Repositories'

   
        bars.y_labels = (1, 5, 10, 50, 100, 500, 1000, 5000)
        for item in repo_data:
            bars.add(item['name'], int(item['size']))

    
        context = {
            'chart' : bars.render_data_uri(),
            'title' : "Github Repo Size",
            }
    return render(request, 'pages/dashboard.html', context) 
