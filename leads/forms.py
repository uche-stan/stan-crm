from django import forms 
from .models import Lead, User

from django.contrib.auth.forms import UserCreationForm



class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'
        
        
# Becasue we created our own User, we also need to create our sign up form
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",) 
        