from __future__ import  unicode_literals, absolute_import
from django.shortcuts import render
from .forms import UserRegForm, UserLoginForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import Application, Configuration
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

# Create your views here.


def main(request):
    
    
    
    return render(request, 'main.html')

def appint(request):
    
    return render(request, 'appint.html')

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
    

    





