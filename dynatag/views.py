from django.shortcuts import render
from .forms import UserRegForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import Profile
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def account_register(request):
    
    if request.method == 'POST':
        
        #return HttpResponse("I am Register post!")
        user_form = UserRegForm(request.POST)
        
        if user_form.is_valid():
            
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            
            profile = Profile.objects.create(user=new_user)
            
            messages.add_message(request, messages.SUCCESS, u'Register Successfully!')
            
            return HttpResponseRedirect(reverse('accountregister'))
            #return HttpResponseRedirect('/dynatag/account/register/')
        
    else:
        
        #return HttpResponse("I am Register get!")
        user_form = UserRegForm()
        
    return render(request, 'register.html', {'regform': user_form})

def account_info(request):
    
    return "I am account Info"

def account_edit(request):
    
    return "I am Account Edit"