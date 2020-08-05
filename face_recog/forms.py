from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from . models import *
class CreateUserForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))
   
    class Meta:
        model=User
        fields=['username','email','password1','password2',]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'E-mail'}),
            
        }
class profile_form(ModelForm):
    class Meta:
        model=Profile
        fields='__all__'
        exclude=['user',]