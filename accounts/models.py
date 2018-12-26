from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=30, blank=False)
    done = models.BooleanField(blank=False, default=False)
    
    
class Profile(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    website = models.CharField(max_length=50, blank=True)
    publicinfo = models.TextField(blank=True)