
from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from . forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User


def register(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()

                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password2')
                user = authenticate(username=username, password=password)
                login(request, user)
                messages.success(request, 'Wow!, first time login, Profile succesfully created')
                return redirect('profile')
                
    context = {
        'form': form,
    }
    return render(request, 'front-end/register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')



def doLogin(request):

    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                messages.success(request, 'Welcome back ' + user.username)
                if request.user.profile.is_admin == True:
                    return redirect('dashboard')
                return redirect('profile')
            else:
                messages.warning(request, 'Username or password is incorrect!')
                # return render(request, 'profile', context) 

        context = {}
        return render(request, 'front-end/login.html', context) 








# # def myRestaurant(request):



# @login_required(login_url='login')
# def profile(request):
#     mealForm = MealForm()
#     if request.method == 'POST':
#         form = MealForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()

#             messages.success(request, 'Meal successfully added')

#     # def generate_unique_access_code():
#     #     length = 6

#     #     while True:
#     #         access_code = ''.join(random.choices(string.ascii_uppercase, k=length))
#     #         if Restaurant.objects.filter(access_code=access_code).count() == 0:
#     #             break

#     #     return access_code
    
#     if Restaurant.objects.filter(owner=request.user.pk).count() == 0:
#         return redirect('partner')

   
#     context = {
#         'mealForm' : mealForm,
#         'myRestaurant' : Restaurant.objects.filter(owner=request.user.pk),

#     }
#     return render(request, 'dashboard/index.html', context)


    
# @login_required(login_url='login')
# def userSettings(request):
#     context = {}
#     return render(request, 'settings.html', context)
