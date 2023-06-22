from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

# Create your models here.

class User(AbstractUser):
    
    is_organiser = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
    
    
    

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
    date_added = models.DateTimeField(auto_now_add=True)
    source = models.CharField(choices=SOURCE_CHOICES, max_length=100)
    
    # profile_picture = models.ImageField(blank=True, null=True)
    # special_files = models.FileField(blank=True, null=True)
    
    organisations = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    agent = models.ForeignKey("Agent", null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey("Category",null=True, blank=True, related_name="leads", on_delete=models.SET_NULL)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisations = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.email}"
    

class Category(models.Model):
    name = models.CharField(max_length=30) 
    organisations = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
    


def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)       

post_save.connect(post_user_created_signal, sender=User)    
