from staff.models import Staff
from django.http import response
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from dashboard.utils import dashComponents

# Create your views here.
def home(request):
    data = dashComponents(request)
    context = {
        'getStaff':data['getStaff'],
    }
    return render(request, 'front-end/index.html', context)

def staffDetails(request, staff_id):
    staff = get_object_or_404(Staff, first_name=staff_id)

    context = {
        'staff': staff
    }
    return render(request, 'front-end/team-details.html', context)
   




