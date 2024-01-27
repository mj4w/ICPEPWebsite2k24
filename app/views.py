from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from datetime import datetime,timezone
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

    if highlights.date_to <= current_date < highlights.date_from:
        ping = 1
    else:
        ping = 0
    print(ping)
    context = {'highlights': highlights,'ping':ping}
    return render(request,'highlights.html',context)    