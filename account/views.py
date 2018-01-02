from django.shortcuts import render
from .forms import UserRegForm, UserLoginForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import Profile
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User as Member
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    
    return render(request, 'index.html') #HttpResponse('This is the index page!!')

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
            
            return HttpResponseRedirect(reverse('account_register'))
            #return HttpResponseRedirect('/dynatag/account/register/')
        
    else:
        
        #return HttpResponse("I am Register get!")
        user_form = UserRegForm()
        
    return render(request, 'register.html', {'regform': user_form})

def account_profile(request):
    
    return "I am account Info"

def account_edit(request):
    
    return "I am Account Edit"

def account_login(request):
    
    if request.method == 'POST':
    
        m = Member.objects.get(email=request.POST['email'])
        #m = authenticate(email=request.POST['email'], password=make_password(request.POST['password']))
    
        if check_password(request.POST['password'], m.password):
        
            request.session['member_id'] = m.id
            request.session['is_login'] = True
        
            #return vars(m)
            #return HttpResponse(vars(m))
            memberdata = {'username': m.username, 'email': m.email}
            return render(request, 'account_profile.html', {'memberdata': memberdata})
    
        else:
        
            return HttpResponse('Your email or password is not correct!')

    else:
        
        user_form = UserLoginForm()
        
    return render(request, 'login.html', {'loginform': user_form})   

def account_logout(request):
    
    try:
        
        del request.session['member_id']
        
    except KeyError:
        
        pass
    
    return HttpResponse('You are logged out!')    
