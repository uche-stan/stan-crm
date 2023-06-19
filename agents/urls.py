from django.urls import path
from . import views


app_name = 'agents'


urlpatterns = [
    
    path('', views.AgentListView.as_view(), name='agent-list'),
    path('create/', views.AgentCreateView.as_view(), name='agent-create'),
    path('agent-detail/<int:pk>', views.AgentDetailView.as_view(), name='agent-detail'),
    path('agent-update/<int:pk>', views.AgentUpdateView.as_view(), name='agent-update'),
    path('agent-confirm-delete/<int:pk>', views.AgentConfirmDeleteView.as_view(), name='agent-confirm-delete')
]
