from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
from django.contrib import messages
from django.core.exceptions import ValidationError

class RegisterForm(UserCreationForm):
    email = forms.CharField(
        label='email',
        widget=forms.EmailInput(attrs={'class': 'input'})
    )
    username = forms.CharField(
        label='username',
        widget=forms.TextInput(attrs={'class':'input'})
    )
    password1 = forms.CharField(
        label='password1',
        widget=forms.PasswordInput(attrs={'class': 'input'})
    )
    password2 = forms.CharField(
        label='password2',
        widget=forms.PasswordInput(attrs={'class':'input'})
    )

    class Meta: 
        model = User
        fields = ('email', 'username', 'password1', 'password2', 'orgbox')
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email:
            email = email.lower()
            if not email.endswith('@bulsu.edu.ph'):
                raise ValidationError('Only email addresses with @bulsu.edu.ph domain are allowed.')

        return email
        
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='username',
        widget=forms.TextInput(attrs={'class': 'input'})
    )
    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput(attrs={'class':'input'})
    )
