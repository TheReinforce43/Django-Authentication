from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms


class RegistrationForm(UserCreationForm):

    first_name=forms.CharField(widget=forms.TextInput(attrs={'id':'required'})) 
    last_name=forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))   

    class Meta:

    
      
        fields=['username','first_name','last_name','email']

        help_texts={
            'first_name':'Please enter your first name',
            'last_name':'Please enter your last name',
        }


class ChangeUserData(UserChangeForm):
    
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']


