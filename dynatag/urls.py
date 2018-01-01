from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
#from auth import views as local_auth_views
from dynatag import  views as dynatag_views

urlpatterns = [
    
    path('main/', dynatag_views.main),
    
    ]