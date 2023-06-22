from django.urls import path
from . import views

app_name = 'leads'

urlpatterns = [
    # path('',views.index, name='home' ),
    path('',views.HomePageView.as_view(), name='home' ),
    # path('lead-list/', views.lead_list, name='lead-list'),
    path('lead-list/', views.LeadListView.as_view(), name='lead-list'),
    # path('lead-list/<int:pk>', views.lead_detail_list, name='lead-detail'),
    path('lead-list/<int:pk>', views.LeadDetailView.as_view(), name='lead-detail'),
    # path('lead-create/', views.lead_create, name='lead-create'),
    path('lead-create/', views.LeadCreateView.as_view(), name='lead-create'),
    path('created-successfully/', views.SuccessCreateView.as_view()),
    # path('lead-update/<int:pk>', views.lead_update, name='lead-update'),
    path('lead-update/<int:pk>', views.LeadUpdateView.as_view(), name='lead-update'),
    path('lead-confirm-update/', views.lead_update_alert, name='lead-update-alert'),
    # path('lead-confirm-delete/<int:pk>', views.lead_delete, name='lead-confirm-delete'),
    path('lead-confirm-delete/<int:pk>', views.LeadDeleteView.as_view(), name='lead-confirm-delete'),
    path('lead-delete-alert/', views.delete_alert, name='delete-alert'),
    
    path('assign-agent/<int:pk>', views.AssignAgentView.as_view(), name='assign-agent'),
    path('agent-assigned-update/', views.agent_assigned_alert, name='agent-assigned-update'),
    
    
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>', views.CategoryDetailView.as_view(), name='category-detail'),
    
    path('category/<int:pk>',views.LeadCategoryUpdateView.as_view(), name='lead-category-update'),
    path('category-confirm-update/', views.category_confirm_update, name='category-confirm-update'),

    
    
    
    
    
]
