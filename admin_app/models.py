from django.db import models

# Create your models here.

class Door(models.Model):
    image = models.ImageField(upload_to='admin_app/door')
    head = models.CharField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    
class Window(models.Model):
    image = models.ImageField(upload_to='admin_app/Window')
    head = models.CharField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    
class Project(models.Model):
    image = models.ImageField(upload_to='admin_app/projects')
    head = models.CharField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    status = models.BooleanField(default=False)