from django.contrib import admin
from .models import User, Lead, Agent

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name' )
    
@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ( 'first_name', 'last_name','age','email','phone', 'description','profile_picture','source', 'agent', )    


    
# @admin.register(Agent)
# class AgentAdmin(admin.ModelAdmin):
#     list_display = ( 'first_name', 'last_name',)        

admin.site.register(Agent)


# admin.site.register(UserProfile)