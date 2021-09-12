from django.urls import path
from django.conf.urls import include, url
from app import views

urlpatterns = [
    path('', views.home, name="home"), 
    path('staff/<str:staff_id>/', views.staffDetails, name='staffDetails'),
]
