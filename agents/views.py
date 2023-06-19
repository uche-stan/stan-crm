import random

from typing import Any
from django.db.models.query import QuerySet
from .forms import AgentModelForm
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .mixins import OrganiserAndLoginRequiredMixin
from django.core.mail import send_mail


# Create your views here.

class AgentListView(OrganiserAndLoginRequiredMixin, generic.ListView):
    template_name = 'agents/agent_list.html'
    context_object_name = 'agents'
    
    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisations=organisation)
    

class AgentCreateView(OrganiserAndLoginRequiredMixin, generic.CreateView):
    template_name = 'agents/agent_create.html'  
    form_class = AgentModelForm
    
    success_url = '/agents/'
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organiser = False
        user.save()
        user.set_password(f"{random.randint(0, 1000000)}")
        Agent.objects.create(
            user=user,
            organisations=self.request.user.userprofile
        )
        send_mail(
            subject='You are invited to be an agent',
            message='You were added as an agent in StansCRM. Please click the link to login',
            from_email='admin@stanscrm.com',
            recipient_list=[user.email]
        )
        return super(AgentCreateView, self).form_valid(form)
    
    
    # def form_valid(self, form):
    #     agent = form.save(commit=False)
    #     agent.organisations = self.request.user.userprofile
    #     agent.save()
    #     return super(AgentCreateView, self).form_valid(form)
    
    
class AgentDetailView(OrganiserAndLoginRequiredMixin, generic.DetailView):
    template_name = 'agents/agent_detail.html'   
    context_object_name = 'agent'
    
    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisations=organisation)



class AgentUpdateView(OrganiserAndLoginRequiredMixin, generic.UpdateView):
    template_name = 'agents/agent_update.html' 
    model = Agent
    fields = '__all__'  
    success_url = '/agents/'
    
    
    
class AgentConfirmDeleteView(OrganiserAndLoginRequiredMixin, generic.DeleteView):
    template_name = 'agents/agent_confirm_delete.html'  
    context_object_name = 'agent' 
    success_url = '/agents/'
    
    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisations=organisation)