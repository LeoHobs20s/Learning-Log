from django import forms
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control text-dark mb-4 mt-2', 'placeholder':'Enter Your Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control text-dark mb-4 mt-2', 'placeholder':'Enter Your Password'}))


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'class':'form-control text-bg-white mt-2 mb-3',
        'label':'username',
        'placeholder':'Enter your username',
        'type':'text'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control text-bg-white mt-2 mb-3',
        'placeholder':'Enter your password'
    }), label='Password')

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control text-bg-white m',
        'placeholder':'Confirm your password'
    }), label='Confirm Password')
    
    