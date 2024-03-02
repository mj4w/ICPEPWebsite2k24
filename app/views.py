from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from datetime import datetime,timezone
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import auth, User
# Create your views here.
def home(request):
    banner = Banner.objects.first()
    aboutpic = AboutPic.objects.first()
    highlights = HighlightsEvent.objects.all()
    softwaretools = SoftwareTools.objects.all()
    context = {
        'banner': banner,
        'aboutpic': aboutpic,
        'highlights': highlights,
        'softwaretools': softwaretools
    }

    return render(request,'homepage.html',context)

def resources(request):
    return render(request,'resources_docu.html')

def highlights(request,pk):
    current_date = datetime.now().date()
    highlights = HighlightsEvent.objects.get(id=pk)

    if highlights.date_to is not None and highlights.date_from is not None:
        if highlights.date_to <= current_date < highlights.date_from:
            ping = 1
        else:
            ping = 0
    else:
        ping = 0

    print(ping)
    context = {'highlights': highlights,'ping':ping}
    return render(request,'highlights.html',context)


# accounts
def login_user(request):
    if request.method =="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password= password)
            if user is not None:
                login(request,user)
                messages.success(request, f'Ohayo!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid Username or password!')
        else:
            messages.error(request, 'Invalid Username or password! ')
    form = AuthenticationForm()
    return render(request, 'accounts/login.html')

def register_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST ['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username exist, type another one')
                return redirect('register-user')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                #log user in and redirect to settings page
                user_login = auth.authenticate(username=username, password= password)
                auth.login(request, user_login)

                return redirect('home')
        else:
            messages.info(request,'Check Password if correct')
            return redirect ('register-user')
    return render(request, 'accounts/register.html')


def logout_user(request):
    logout(request)
    messages.success(request,'Thankyou For Visiting!')
    return redirect('/')


# coming soon
def coming_soon(request):
    return render(request, 'coming_soon/coming_soon.html')