from django.shortcuts import render
from .forms import UserRegForm, UserLoginForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import Profile
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User as Member
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from dynatag import urls
from dynaplus import settings as Settings

# Create your views here.


def main(request):
    
    
    
    return render(request, 'main.html')

def appint(request):
    
    return render(request, 'appint.html')

def configuration(request):
    
    return render(request, 'configuration.html')