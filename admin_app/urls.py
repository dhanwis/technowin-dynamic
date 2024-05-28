from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    
    path('doors/', door_list, name='door_list'),
    path('doors/add/', door_add, name='door_add'),
    path('doors/<int:door_id>/view/', door_view, name='door_view'),
    path('doors/<int:door_id>/edit/', door_edit, name='door_edit'),
    path('doors/<int:door_id>/delete/', door_delete, name='door_delete'),
    
    path('windows/', window_list, name='window_list'),
    path('windows/add/', window_add, name='window_add'),
    path('windows/<int:window_id>/view/', window_view, name='window_view'),
    path('windows/<int:window_id>/edit/', window_edit, name='window_edit'),
    path('windows/<int:window_id>/delete/', window_delete, name='window_delete'),
    
    path('projects/', project_list, name='project_list'),
    path('projects/add/', project_add, name='project_add'),
    path('projects/<int:project_id>/view/', project_view, name='project_view'),
    path('projects/<int:project_id>/edit/', project_edit, name='project_edit'),
    path('projects/<int:project_id>/delete/', project_delete, name='project_delete'),
    
]