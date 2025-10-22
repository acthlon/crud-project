from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model

from django.contrib.auth.forms import AuthenticationForm 
from django.forms.widgets import TextInput, PasswordInput

from .models import Account

class CreateUserForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username','password1','password2')

class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget = TextInput)
    password = forms.CharField(widget=PasswordInput)         

class CreateAccountForm(forms.ModelForm):

    class Meta:

        model = Account
        fields = ['first_name','last_name','email','phone','address','city','province','country']
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'input-class'}),
            'last_name':forms.TextInput(attrs={'class':'input-class'}),
            'email': forms.EmailInput(attrs={'class':'input-class'}),
            'phone':forms.TextInput(attrs={'class':'input-class'}),
            'address': forms.TextInput(attrs={'class':'input-class'}),
            'city':forms.TextInput(attrs={'class':'input-class'}),
            'province': forms.TextInput(attrs={'class':'input-class'}),
            'country':forms.TextInput(attrs={'class':'input-class'})
        }



class UpdateAccountForm(forms.ModelForm):

    class Meta:

        model = Account
        fields = ['first_name','last_name','email','phone','address','city','province','country']
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'input-class'}),
            'last_name':forms.TextInput(attrs={'class':'input-class'}),
            'email': forms.EmailInput(attrs={'class':'input-class'}),
            'phone':forms.TextInput(attrs={'class':'input-class'}),
            'address': forms.TextInput(attrs={'class':'input-class'}),
            'city':forms.TextInput(attrs={'class':'input-class'}),
            'province': forms.TextInput(attrs={'class':'input-class'}),
            'country':forms.TextInput(attrs={'class':'input-class'})
        }
