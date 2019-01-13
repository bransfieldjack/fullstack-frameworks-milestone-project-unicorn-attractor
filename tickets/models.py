from django.db import models


STATUS_CHOICES = (
    ('assigned','ASSIGNED'),
    ('in progess','IN PROGRESS'),
    ('completed', 'COMPLETED'),
)

    
class Bugs(models.Model):    # Bugs Model, used to register a new bug. 
    title = models.CharField(max_length=50, default='')
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    likes= models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices = STATUS_CHOICES, default='assigned')
    
    
    def __str__(self):
        return self.title
        
    
class Features(models.Model):   # Features Model, used to request new feature additions. 
    title = models.CharField(max_length=50, default='')
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    likes= models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices = STATUS_CHOICES, default='assigned')
    
    
    def __str__(self):
        return self.title
        
        
class Comments(models.Model):   # Comments Model, used to store comments for either a bug or feature using a foreign key
    feature = models.ForeignKey(Features, null=True)
    bug = models.ForeignKey(Bugs, null=True)
    message = models.TextField()
    user = models.CharField(max_length=50, default='')
    
    
    def __str__(self):
        return self.message