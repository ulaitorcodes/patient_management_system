from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Staff(models.Model):
    GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'),
    )
    STAFF_TYPE_CHOICES = (
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
    )
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, null=True, unique=True)
    last_name = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=50, null=True)
    phone = models.CharField(max_length=20, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True)
    staff_type= models.CharField(choices=STAFF_TYPE_CHOICES, max_length=15, null=True)
    age = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)
    photo = models.ImageField(upload_to='media/staff/', null=True)
    joined_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


class Doctor(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.staff}"