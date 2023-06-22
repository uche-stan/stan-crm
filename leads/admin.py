from django.contrib import admin
from .models import (
    User, 
    Lead, 
    Agent, 
    UserProfile, 
    Category
)

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name' )
    
@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ( 'first_name', 'last_name','age','email','phone', 'description','date_added','source','organisations', 'agent','category' )    


    
# @admin.register(Agent)
# class AgentAdmin(admin.ModelAdmin):
#     list_display = ( 'first_name', 'last_name',)        

admin.site.register(Agent)


admin.site.register(UserProfile)

admin.site.register(Category)

    