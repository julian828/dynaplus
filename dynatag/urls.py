from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
#from auth import views as local_auth_views
from dynatag import  views as dynatag_views

app_name = 'dynatag'

urlpatterns = [
    
    path('', dynatag_views.main, name='dynatag_main'),
    path('appint/', dynatag_views.appint, name='dynatag_appint'),
    path('configuration/', dynatag_views.configuration, name='dynatag_configuration'),
    
    ]