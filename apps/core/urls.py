from django.urls import path

from apps.core import views

urlpatterns = [
   
    path('', views.git_repo_home, name="home"),
    path('list/dash/<int:git_id>/', views.git_dashboard),
    path('list/create/', views.git_repo_create),
    ]
   
