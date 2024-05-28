from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('doors/', doors, name='doors'),
    path('windows/', windows, name='windows'),
    path('projects/', projects, name='projects'),
    path('services/', services, name='services'),
    path('contact/', contact, name='contact')
]