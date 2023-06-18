from django.forms.models import BaseModelForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Lead
from .forms import LeadForm, CustomUserCreationForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


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
    model = Lead
    context_object_name = "leads"
    
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
    model = Lead
    context_object_name = "lead"

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
class LeadCreateView(LoginRequiredMixin, generic.CreateView):
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
class LeadUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'update.html'
    model = Lead
    fields = '__all__'
    context_object_name = 'lead'
    success_url = '/lead-confirm-update/'


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
class LeadDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'confirm_delete.html'
    model = Lead
    context_object_name = 'lead'
    success_url = '/lead-delete-alert/'



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


# class SignupFormView(generic.TemplateView):
#     template_name = 'registration/signup.html'

class SignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    success_url = '/login'