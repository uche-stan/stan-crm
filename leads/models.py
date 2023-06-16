from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class Lead(models.Model):
    
    SOURCE_CHOICES = (
        
        ('Facebook', 'Facebook'),
        ('Instagram', 'Instagram'),
        ('Google', 'Google'),
        ('YouTube', 'YouTube'),
        ('Newsletter', 'Newsletter'),
    )
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    
    phoned = models.BooleanField(default=False)
    source = models.CharField(choices=SOURCE_CHOICES, max_length=100)
    
    profile_picture = models.ImageField(blank=True, null=True)
    special_files = models.FileField(blank=True, null=True)
    
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
    


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    
        
    
