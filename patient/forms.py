from django.contrib.auth import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from patient.models import Appointment
# from betterforms.multiform import MultiModelForm

# form classes
class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'time', 'doctor', 'message', 'user']
        widgets = {
            'user': forms.HiddenInput(attrs={'class': 'form-control', 'type': 'hidden', 'placeholder': ''}),
            'date': forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time','class': 'form-control' }),
            'doctor': forms.Select(attrs={'type': 'text', 'class': 'form-control'}),
            'message': forms.TextInput(attrs={'type': 'textarea', 'class': 'form-control', 'placeholer': 'Additional Message'}),
            
        }


