from django.shortcuts import render
from admin_app.models import *

# Create your views here.

def home(request):
    current_page = 'home'
    
    context = {
        'current_page': current_page,
        
    }
    return render(request, 'user_app/pages/home.html', context)



def about(request):
    current_page = 'about'
    context = {
        'current_page': current_page,
    }
    return render(request, 'user_app/pages/about.html', context)


def doors(request):
    current_page = 'doors'
    doors = Door.objects.all()
    context = {
        'current_page': current_page,
        'doors':doors
    }
    return render(request, 'user_app/pages/doors.html', context)


def windows(request):
    current_page = 'windows'
    windows = Window.objects.all()
    context = {
        'current_page': current_page,
        'windows':windows
    }
    return render(request, 'user_app/pages/windows.html', context)


def projects(request):
    current_page = 'projects'
    projects = Project.objects.all()
    context = {
        'current_page': current_page,
        'projects' : projects
    }
    return render(request, 'user_app/pages/projects.html', context)


def services(request):
    current_page = 'services'
    context = {
        'current_page': current_page,
    }
    return render(request, 'user_app/pages/services.html', context)


def contact(request):
    current_page = 'contact'
    context = {
        'current_page': current_page,
    }
    return render(request, 'user_app/pages/contact.html', context)