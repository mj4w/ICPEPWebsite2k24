from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from datetime import datetime,timedelta,timezone
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.core.exceptions import SuspiciousOperation
from .forms import *
# Create your views here.
def home(request):
    current_date = datetime.now().date()
    
    banner = Banner.objects.first()
    aboutpic = AboutPic.objects.first()
    highlights = HighlightsEvent.objects.all().order_by('-date_from')
    softwaretools = SoftwareTools.objects.all()

    context = {
        'banner': banner,
        'aboutpic': aboutpic,
        'highlights': highlights,
        'softwaretools': softwaretools,
    }

    return render(request,'homepage.html',context)

def resources(request):
    resource_docu = SoftwareToolsResource.objects.all()
    return render(request,'resources_docu.html',{'resource_docu':resource_docu})

def highlights(request,pk):
    current_date = datetime.now().date()
    highlights = HighlightsEvent.objects.get(id=pk)

    if highlights.date_to is not None and highlights.date_from is not None:
        if highlights.date_to <= current_date <= highlights.date_from:
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
    try: 
        if request.method == 'POST':
            form_login = LoginForm(request.POST or None, data=request.POST)
            if form_login.is_valid():
                user = authenticate(request, username=form_login.cleaned_data['username'], password=form_login.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    messages.success(request,'Successfully Login!')
                    return redirect('home')
            else:
                # Form is not valid
                messages.error(request, 'Login Error: Please enter valid credentials.')
    except SuspiciousOperation as e:
        messages.error(request, f'CSRF Verification Failed: {str(e)}')
        return redirect('home')
    form_login = LoginForm()
    return render(request, 'accounts/login.html',{'form_login': form_login})

def register_user(request):
    try:
        if request.method == 'POST':
            form_register = RegisterForm(request.POST or None)
            if form_register.is_valid():
                user = form_register.save()
                login(request, user)
                messages.success(request, 'You have been registered! Login Now!')
                return redirect('home')
            else:
                for field, errors in form_register.errors.items():
                    for error in errors:
                        messages.error(request, f"Registration Error: {field.capitalize()} - {error}")
    except SuspiciousOperation as e:
        messages.error(request, f'CSRF Verification Failed: {str(e)}')
        return redirect('home')
    form_register = RegisterForm()
    return render(request, 'accounts/register.html',{'form_register': form_register})


def logout_user(request):
    logout(request)
    messages.success(request,'Thankyou For Visiting!')
    return redirect('/')


# coming soon
def coming_soon(request):
    return render(request, 'coming_soon/coming_soon.html')