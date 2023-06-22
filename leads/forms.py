from django import forms 
from .models import Lead, User, Agent, Category

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




class AssignAgentForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=Agent.objects.none())
    
    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request")
        agents = Agent.objects.filter(organisations=request.user.userprofile)
        super(AssignAgentForm, self).__init__(*args, **kwargs)
        self.fields["agent"].queryset = agents
        
        


class LeadcategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ("category",)
            