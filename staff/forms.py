from staff.models import Staff
from django.contrib.auth import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from patient.models import Appointment
# from betterforms.multiform import MultiModelForm

# form classes
class StaffForm(ModelForm):
    class Meta:
        model = Staff
        fields = ['first_name', 'last_name', 'email', 'phone', 'gender', 'staff_type', 'age', 'address', 'photo', 'joined_at']
        widgets = {

            'first_name': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholer': 'Additional Message'}),
            'last_name': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholer': 'Additional Message'}),
            'email': forms.TextInput(attrs={'type': 'email', 'class': 'form-control', 'placeholer': 'Additional Message'}),
            'phone': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholer': 'Additional Message'}),
            'gender': forms.Select(attrs={'type': 'text', 'class': 'form-control'}),
            'staff_type': forms.Select(attrs={'type': 'text', 'class': 'form-control'}),
            'joined_at': forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}),
            'age': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'address': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control', 'type': 'file'}),

            # 'photo': forms.ImageField(attrs={'type':'file', 'class':'form-control'})
        }





    # first_name = models.CharField(max_length=20)
    # last_name = models.CharField(max_length=20)
    # email = models.EmailField(max_length=50)
    # phone = models.CharField(max_length=20)
    # gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    # staff_type= models.CharField(choices=STAFF_TYPE_CHOICES, max_length=15)
    # age = models.CharField(max_length=50)
    # address = models.CharField(max_length=50)
    # photo = models.ImageField(upload_to='media/staff/', null=True)
