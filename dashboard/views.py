from django.shortcuts import render, redirect
from patient.models import *
from .utils import *
from staff.models import Staff
from staff.forms import StaffForm
from django.contrib import messages

# Create your views here.
def dashboard(request):
    data = dashComponents(request)
    
    context = {
        'appointments_no':data['appointments_no'],
        'doctors_no': data['doctors_no'],
        'appointments':data['appointments'],
        'doctors': data['doctors'],
        'getStaff': data['getStaff'],

    }
    return render(request, 'back-end/hospital-index.html', data)


def addStaff(request):
    form = StaffForm()
    data = dashComponents(request)
    if request.method == 'POST':
        form = StaffForm(request.POST, request.FILES)
        # Restaurant.objects.get('owner') == request.auth
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff successfully added')
            return redirect('dashboard')

    context = {
        'appointments_no':data['appointments_no'],
        'doctors_no': data['doctors_no'],
        'appointments':data['appointments'],
        'doctors': data['doctors'],
        'form': form,
    }
    return render(request, 'back-end/add-member.html', context)
