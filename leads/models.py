from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.user.username
    
    
    
    

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
    email = models.EmailField(default="lead@example.com")
    phone = models.CharField(max_length=20, default=+44)
    description = models.CharField(max_length=255, blank=True, null=True)
    
    phoned = models.BooleanField(default=False)
    source = models.CharField(choices=SOURCE_CHOICES, max_length=100)
    
    profile_picture = models.ImageField(blank=True, null=True)
    special_files = models.FileField(blank=True, null=True)
    
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # organisations = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user}"
    
    
        
    
