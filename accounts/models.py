from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    name = models.CharField(max_length=30, blank=False) # Model used during development for testing purposes. 
    done = models.BooleanField(blank=False, default=False)
    
    
class Profile(models.Model):    # Model under development for release in a future iteration. Possibly used with/extending the User auth model. 
    upload = models.FileField()
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=50)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    website = models.CharField(max_length=50, blank=True)
    publicinfo = models.TextField(blank=True)
