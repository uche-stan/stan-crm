
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import (
    LoginView, 
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
    
)
from leads import views


# app_name = 'leads'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('leads.urls', namespace='leads')),
    path('signup/',views.SignupView.as_view(), name='signup' ),
    path('password-reset/', PasswordResetView.as_view(), name='password-reset'),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(), name='password_reset_confirm' ),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    
    path('agents/', include('agents.urls', namespace='agents')),
    
]
