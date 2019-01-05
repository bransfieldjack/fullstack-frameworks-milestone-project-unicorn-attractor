from django.db import models

    
class Bugs(models.Model):
    title = models.CharField(max_length=50, default='')
    reported_by = models.CharField(max_length=50, default='')
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)  # As soon as the record is created the current date and time will be added to the field. 
    views = models.IntegerField(default=0)  # Integer field which records number of views. (Starts at 0)
    comments = models.TextField(default='')
    user = models.CharField(max_length=50, default='')
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
    feature = models.ForeignKey(Features)
    message = models.CharField(max_length=50, default='')
    
    
    def __str__(self):
        return self.message