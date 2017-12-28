from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
#from auth import views as local_auth_views
from account import views as account_views

urlpatterns = [
    
    path('', account_views.index, name='index'),
    
    path('profile/', account_views.account_profile, name='account'),
    path('edit/', account_views.account_edit, name='account_edit'),
    path('register/', account_views.account_register, name='account_register'),
    
    path('login/', account_views.account_login, name='login'),
    path('logout/', account_views.account_logout, name='logout'),
    path('logout_then_login/', auth_views.logout_then_login, name='logoutthenlogin'),
    
    path('password-change/', auth_views.password_change, name='passwordchange'),
    path('password-change/done/', auth_views.password_change_done, name='password_change_done'),
    
    path('password-reset/', auth_views.password_reset, name='password_reset'),
    path('password-reset/done/', auth_views.password_reset_done, name='password_reset_done'),
    path('password-confirm/(<uidb64>/<token>/', auth_views.password_reset_confirm, name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.password_reset_complete, name='password_reset_complete')
    
    
    ]