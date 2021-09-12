
from django.urls import path

from django.conf.urls import include, url

from . import views


urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('staff/add/', views.addStaff, name="addStaff")
   
]