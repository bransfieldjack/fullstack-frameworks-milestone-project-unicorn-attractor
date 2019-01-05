from django.db import models

    
class Bugs(models.Model):
    title = models.CharField(max_length=50, default='')
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    likes= models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.title
        
    
class Features(models.Model):
    title = models.CharField(max_length=50, default='')
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    likes= models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.title
        
        
class Comments(models.Model):
    feature = models.ForeignKey(Features, null=True)
    bug = models.ForeignKey(Bugs, null=True)
    message = models.TextField()
    user = models.CharField(max_length=50, default='')
    
    
    def __str__(self):
        return self.message