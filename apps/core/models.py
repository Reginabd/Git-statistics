from django.db import models

from apps.accounts.models import User

class Gitstats(models.Model):
    user_name = models.CharField(max_length=30)
    git_profile = models.CharField(max_length=64)
    panel_type = models.CharField(max_length=64)
    git_profile_description = models.CharField(max_length=160)
    

    created = models.DateTimeField(auto_now_add=True) 
    last_modified = models.DateTimeField(auto_now=True)


    creator_user = models.ForeignKey(User, on_delete=models.CASCADE)

  

