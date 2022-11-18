from django.shortcuts import render
from app_1.forms import UserForm, HealthForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
    return render(request,'app_1/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']

        if User.objects.filter(username=username):
            return HttpResponseRedirect(reverse('home'))

        if User.objects.filter(email=email).exists():
            return HttpResponseRedirect(reverse('home'))

        if len(username)>20:
            return HttpResponseRedirect(reverse('home'))
    
        if not username.isalnum():
            return HttpResponseRedirect(reverse('home'))

        if password != password_2:
            return HttpResponseRedirect(reverse('home'))

        user_form = UserForm({'username': username,
        'password': password, 
        'first_name': first_name, 
        'last_name': last_name, 
        'email': email})

        health_form = HealthForm({'dob':dob, 
        'age': age, 
        'gender': gender})

        if user_form.is_valid() and health_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.is_active = True
            user.save()
            
            Health = health_form.save(commit=False)
            Health.user = user
            Health.save()
        else:
            print(user_form.errors, health_form.errors)
    
    else:
        user_form = UserForm()
        health_form = HealthForm()

    return render(request,'app_1/registration.html',{
        'user_form':user_form,
        'health_form':health_form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Your account is inactive!!')
        
        else:
            print("Someone tried to login and failed!!")
            print("They used the username:{} and password:{}".format(username, password))
            return HttpResponse('Bad Credentials')

    else:
        return render(request, 'app_1/login.html',{})       


        




