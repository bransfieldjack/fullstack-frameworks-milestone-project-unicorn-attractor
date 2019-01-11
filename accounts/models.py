from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    name = models.CharField(max_length=30, blank=False)
    done = models.BooleanField(blank=False, default=False)
    
    
class Profile(models.Model):
    upload = models.FileField()
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=50)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    website = models.CharField(max_length=50, blank=True)
    publicinfo = models.TextField(blank=True)
