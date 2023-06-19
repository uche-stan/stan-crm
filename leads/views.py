from typing import Any, Dict
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Lead
from .forms import LeadForm, CustomUserCreationForm, AssignAgentForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from agents.mixins import OrganiserAndLoginRequiredMixin


# Create your views here.



# Home Page View
######################################################

#generic base view
###################
class HomePageView(generic.TemplateView):
    template_name = 'index.html'

#function base view
###################
def index(request):
    return render(request, 'index.html')

######################################################



# List View 
######################################################

#generic base view
###################
class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = 'lead_list.html'
    context_object_name = "leads"
    
    def get_queryset(self):
        user = self.request.user
        
        #initial queryset for the entire organisation
        if user.is_organiser:
            queryset = Lead.objects.filter(organisations=user.userprofile, agent__isnull=False )
        else:
            queryset = Lead.objects.filter(organisations=user.agent.organisations, agent__isnull=False)
            #filter for the agent that is loggedin
            queryset = queryset.filter(agent__user=user)
            
        return queryset    
    
    # seperate assigned and unassigned leads
    
    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super(LeadListView, self).get_context_data(**kwargs)
        if user.is_organiser:
            queryset = Lead.objects.filter(
                organisations=user.userprofile, 
                agent__isnull=True,
            )
            context.update(
                {
                    'unassigned_leads': queryset
                }
            )
        return context
        
        
#function base view
###################
def lead_list(request):
    
    leads = Lead.objects.all()
    context = {'leads': leads}  
    return render(request, 'lead_list.html', context)


######################################################




# List Detail View 
######################################################

#generic base view
###################
class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'detail_list.html'
    context_object_name = "lead"
    
    def get_queryset(self):
        user = self.request.user
        
        #initial queryset for the entire organisation
        if user.is_organiser:
            queryset = Lead.objects.filter(organisations=user.userprofile)
        else:
            queryset = Lead.objects.filter(organisations=user.agent.organisations)
            #filter for the agent that is loggedin
            queryset = queryset.filter(agent__user=user)
            
        return queryset   

#function base view
###################
def lead_detail_list(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    context = {'lead': lead}
    return render(request, 'detail_list.html', context)
######################################################



# Create View 
######################################################

#generic base view
###################
class LeadCreateView(OrganiserAndLoginRequiredMixin, generic.CreateView):
    template_name = 'lead_create.html'
    form_class = LeadForm
    # model = Lead
    # fields = '__all__'
    success_url = '/created-successfully/'
   
    
    # send email
    def form_valid(self, form):
        send_mail(
            subject='New lead created',
            message='visit site to view lead',
            from_email='test@test.com',
            recipient_list=['test2@test.com']
        )
        return super(LeadCreateView, self).form_valid(form)
     

#function base view
###################
def lead_create(request):
    form =  LeadForm()
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
    
            return render(request, 'success.html')
    context = {'form': form}    
    return render(request, 'lead_create.html', context)    
######################################################



class SuccessCreateView(generic.TemplateView):
    template_name = 'success.html'
    
    

# Update View 
######################################################   

#generic base view
###################
class LeadUpdateView(OrganiserAndLoginRequiredMixin, generic.UpdateView):
    template_name = 'update.html'
    fields = '__all__'
    context_object_name = 'lead'
    success_url = '/lead-confirm-update/'
    
    def get_queryset(self):
        user = self.request.user
        #initial queryset for the entire organisation
        return Lead.objects.filter(organisations=user.userprofile)
            
    


#function base view
################### 
def lead_update(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    form = LeadForm(instance=lead)
    if request.method == 'POST':
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('/lead-confirm-update/')
    
    context = {'form': form, 'lead': lead}
    return render(request, 'update.html', context)
######################################################



def lead_update_alert(request):
    return render(request, 'lead_update_alert.html')
    

# Delete View 
######################################################  

#generic base view
###################
class LeadDeleteView(OrganiserAndLoginRequiredMixin, generic.DeleteView):
    template_name = 'confirm_delete.html'
    context_object_name = 'lead'
    success_url = '/lead-delete-alert/'
    
    def get_queryset(self):
        user = self.request.user
        #initial queryset for the entire organisation
        return Lead.objects.filter(organisations=user.userprofile)
            
#function base view
################### 
def lead_delete(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    if request.method == 'POST':
        lead.delete()
        return redirect('/lead-delete-alert/')
    context = {'lead': lead}
    return render(request, 'confirm_delete.html', context )
######################################################


def delete_alert(request):
    context = {'alert': 'Successfully deleted'}
    return render(request, 'delete_alert.html', context)




# Assign agent view
class AssignAgentView(OrganiserAndLoginRequiredMixin, generic.FormView):
    template_name = 'assign_agent.html'
    form_class = AssignAgentForm
    success_url = '/lead-confirm-update/'
    
    def get_form_kwargs(self, **kwargs):
        kwargs = super(AssignAgentView, self).get_form_kwargs(**kwargs)
        kwargs.update(
            {
            'request': self.request,
    
        }
        ) 
        return kwargs


    def form_valid(self, form):
        agent = form.cleaned_data["agent"]
        lead = Lead.objects.get(id=self.kwargs["pk"])
        lead.agent = agent
        lead.save()
        return super(AssignAgentView, self).form_valid(form)

# class SignupFormView(generic.TemplateView):
#     template_name = 'registration/signup.html'

class SignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    success_url = '/login'
    
    
