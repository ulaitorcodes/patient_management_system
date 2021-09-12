from django.shortcuts import render, redirect
from patient.models import *



def dashComponents(request):
    appointments_no = Appointment.objects.all().count()
    doctors_no = Doctor.objects.all().count()

    # select all
    doctors = Doctor.objects.all()
    appointments = Appointment.objects.all()
    getStaff  = Staff.objects.all()

    return {
        'appointments_no': appointments_no,
        'doctors_no': doctors_no,
        'doctors': doctors,
        'appointments': appointments,
        'getStaff': getStaff,
    }
