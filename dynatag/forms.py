from django import forms
from django.forms import ModelForm
from django.conf import settings
from django.contrib.auth.models import User


class UserRegForm(forms.ModelForm):
    
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
    
    class Meta:
        
        model = User
        fields = ('username', 'email')
        
    def clean_password2(self):
        
        cd = self.cleaned_data
        
        if cd['password'] != cd['password2']:
            
            raise forms.validationError(u'Password Incorrect!')
        
        return cd['password2']