from django.contrib.auth.models import User
from django.db import models
from users.models import *
from staff.models import *
from django.utils import timezone
from django.conf import settings


# Create your models here.
class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    # booked = models.DateTimeField(timezone.now)
    date_booked = models.DateTimeField(auto_now_add=True,null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    message = models.CharField(max_length=500, null=True, blank=True)
