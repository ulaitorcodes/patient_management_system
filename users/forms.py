from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
# from betterforms.multiform import MultiModelForm

# form classes
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'type': 'email', 'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'type': 'text', 'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Last name'}),
            'password1': forms.PasswordInput(attrs={'type': 'password', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'type': 'password', 'placeholder': 'Confirm Password'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'password',
        'placeholder': 'Password'
    }))
