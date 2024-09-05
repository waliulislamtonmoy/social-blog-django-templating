from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms


class SignUpForm(UserCreationForm):
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        
class ProfileChangeForm(UserChangeForm):
    class Meta:
        model=User 
        fields=['email','first_name','last_name','password' ]