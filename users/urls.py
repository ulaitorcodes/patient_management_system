from django.urls import path

from django.conf.urls import include, url

from . import views


urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.doLogin, name='login'),
    path('logout/', views.logoutUser, name='logout'),
   
]