from django.urls import path, include
from django.conf.urls import url
#from django.contrib.auth import views as auth_views
from auth import views as local_auth_views
from dynatag import  views as dynatag_views

urlpatterns = [
    
    path('account/', dynatag_views.account_info, name='account'),
    path('account/edit/', dynatag_views.account_edit, name='accountedit'),
    path('account/register/', dynatag_views.account_register, name='accountregister'),
    
    path('account/login', local_auth_views.login, name='login'),
    path('account/logout', local_auth_views.logout, name='logout'),
    path('account/logout_then_login', local_auth_views.logout_then_login, name='logoutthenlogin'),
    
    path('account/password-change/', local_auth_views.password_change, name='passwordchange'),
    path('account/password-change/done/', local_auth_views.password_change_done, name='password_change_done'),
    
    path('account/password-reset/', local_auth_views.password_reset, name='password_reset'),
    path('account/password-reset/done/', local_auth_views.password_reset_done, name='password_reset_done'),
    path('account/password-confirm/(?P<uidb64>-\w+)/(?P<token>-\w+)/', local_auth_views.password_reset_confirm, name='password_reset_confirm'),
    path('account/password-reset/complete/', local_auth_views.password_reset_complete, name='password_reset_complete')
    
    
    ]