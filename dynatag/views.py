from __future__ import  unicode_literals, absolute_import
from django.shortcuts import render
from .forms import UserRegForm, UserLoginForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import Application, Configuration, Masterdata
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from dynatag import urls
from dynaplus import settings as Settings


from rest_framework import permissions, viewsets
from rest_framework.decorators import ( permission_classes, detail_route)
from rest_framework.response import Response as Restresponse
from .serializers import UserSerializer, ConfigurationSerializer, ApplicationSerializer

from urllib.parse import urlencode
from urllib.request import Request, urlopen

# Create your views here.


def main(request):
    
    
    
    return render(request, 'main.html')

def appint(request):
    
    myappinfo = Masterdata.objects.get(status='active')
    content = {}
    content['clientid'] = myappinfo.clientid
    content['redirecturl'] = myappinfo.redirecturl
    content['responsetype'] = myappinfo.responsetype
    
    return render(request, 'appint.html', content)

def appint_add(request):
    
    content = {}
    c_code = content['code'] = request.GET.get('code')
    c_scope = content['scope'] = request.GET.get('scope').split('|')[0]
    c_appname = content['appname'] = request.GET.get('scope').split('|')[1]
    content['state'] = request.GET.get('state')
    
    try:
        u_user = User.objects.get(username = 'test')
    except Application.DoesNotExist:
        u_user = None
    
    try:
        u_app = Application.objects.get(appname = c_appname, status = 'active', user=u_user)
    except Application.DoesNotExist:
        u_app = None
    
    if u_app:
        
        u_app.code = c_code
        u_app.scope = c_scope
        u_app.save()
        
    else:
        u_app = Application.objects.create()
        u_app.user = u_user
        u_app.appname = c_appname
        u_app.code = c_code
        u_app.scope = c_scope
        u_app.save()
    
    #send post request to get access token
    myappinfo = Masterdata.objects.get(status='active')
    s_url = 'https://api.infusionsoft.com/token'
    
    s_client_id = myappinfo.clientid
    s_client_secret = myappinfo.clientsecret
    s_code = c_code
    s_grant_type = 'authorization_code'
    s_redirect_uri = myappinfo.redirecturl + 'gettoken/'
    post_field = {
        
        'client_id': s_client_id,
        'client_secret': s_client_secret,
        'code': s_code,
        'grant_type': s_grant_type,
        'redirect_uri': s_redirect_uri, 
        
        }
    
    request = Request(s_url, urlencode(post_field).encode())
    result = urlopen(request).read().decode()
    
    return HttpResponse(result)

def configuration(request):
    
    
    
    return render(request, 'configuration.html')

class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

'''    
class UserappViewSet(viewsets.ModelViewSet):
    
    queryset = Userapp.objects.all()
    serializer_class = UserappSerializer
'''
    
class ApplicationViewSet(viewsets.ModelViewSet):
    
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer  
          
class ConfigurationViewSet(viewsets.ModelViewSet):
    
    queryset = Configuration.objects.all()
    serializer_class = ConfigurationSerializer
    

    





