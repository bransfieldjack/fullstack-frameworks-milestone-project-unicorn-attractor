from django.db import models


class Bugs(models.Model):
    title = models.CharField(max_length=50, default='')
    description = models.TextField()
    
    
class Features(models.Model):
    title = models.CharField(max_length=50, default='')
    description = models.TextField()
    
    
    def __str__(self):
        return self.name    # Returns a string with a name. 