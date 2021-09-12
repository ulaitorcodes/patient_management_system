from django.shortcuts import render, redirect, get_object_or_404
from .forms import AppointmentForm
from django.contrib import messages
from .models import Appointment
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')

def profile(request):
    # appointment = get_object_or_404(Appointment, user=request.user.pk)
    myappointments = Appointment.objects.filter(user=request.user.pk).all()
    initial_dict = {
        "user": request.user.pk,
        # "myappointments": myappointments,
    }
    # add the dictionary during initialization
  
    form = AppointmentForm(request.POST or None, initial=initial_dict)
    # form = RestaurantForm()
    if request.method == 'POST':
        # form = AppointmentForm(request.POST or None, initial=initial_dict)

        form = AppointmentForm(request.POST)
        # Restaurant.objects.get('owner') == request.auth
        if form.is_valid():
            # try:
            form.save()
            messages.success(request, 'Your request was sent successfully')
            # except:
            #     pass
            # form.save(commit=False)
            # return redirect('dashboard')
    data = {
        'form': form,
        'myappointments':myappointments,
    }
    return render(request, 'back-end/patient-profile.html', data)
