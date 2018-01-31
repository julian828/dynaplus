from __future__ import unicode_literals, absolute_import
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
#from auth import views as local_auth_views
from dynatag import  views as dynatag_views


from rest_framework import routers


app_name = 'dynatag'

router = routers.DefaultRouter()
router.register('users', dynatag_views.UserViewSet)
#router.register('userapps', dynatag_views.UserappViewSet)
router.register('applications', dynatag_views.ApplicationViewSet)
router.register('configurations', dynatag_views.ConfigurationViewSet)

urlpatterns = [
    
    path('', dynatag_views.main, name='dynatag_main'),
    path('appint/', dynatag_views.appint, name='dynatag_appint'),
    path('configuration/', dynatag_views.configuration, name='dynatag_configuration'),
    path('api/', include(router.urls)),
    #path('api/', include('rest_framework.urls', namespace='rest_framework')),
    
    ]