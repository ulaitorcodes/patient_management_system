from django.urls import path

from django.conf.urls import include, url

from . import views


urlpatterns = [
    path('profile/', views.profile, name="profile"),
    # path('login/', views.doLogin, name='login'),
    # path('logout/', views.logoutUser, name='logout'),
   
]