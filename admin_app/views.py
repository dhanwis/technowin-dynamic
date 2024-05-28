from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

@login_required(login_url='/auth/admin/login/')  
def dashboard(request):
    current_page = 'dashboard'
    door_count = Door.objects.count()
    window_count = Window.objects.count()
    project_count = Project.objects.count()
    context = {
        'current_page': current_page,
        'door_count': door_count,
        'window_count': window_count,
        'project_count': project_count
    }
    return render(request, 'admin_app/pages/dashboard.html', context)




@login_required(login_url='/auth/admin/login/')    
def door_list(request):
    current_page = 'door_list'
    doors = Door.objects.all()
    context = {
        'current_page': current_page,
        'doors': doors
        }
    return render(request, 'admin_app/pages/door_list.html', context)

@login_required(login_url='/auth/admin/login/')
def door_view(request, door_id):
    current_page = 'door_view'
    try:
        door = Door.objects.get(id=door_id)
    except Door.DoesNotExist:
        messages.error(request, 'door not found')
        return redirect('door_list')
    context = {
        'current_page': current_page,
        'door':door
    }
    return render(request, 'admin_app/pages/door_view.html', context)

@login_required(login_url='/auth/admin/login/')
def door_add(request):
    current_page = 'door_add'
    if request.method == 'POST':
        image = request.FILES.get('image') 
        head = request.POST.get('head')
        description = request.POST.get('description')
        
        try:
            door = Door(
                image=image,
                head=head,
                description=description,
            )
            door.save()
            messages.success(request, 'door added successfully')
            return redirect('door_list')
        except Exception as e:
            messages.error(request, f'Error adding door: {e}')
            return redirect('door_add')
        
    context = {
        'current_page': current_page,
    } 
    return render(request, 'admin_app/pages/door_add.html', context)

@login_required(login_url='/auth/admin/login/')
def door_edit(request, door_id):
    current_page = 'door_edit'
    try:
        door = Door.objects.get(id=door_id)
    except Door.DoesNotExist:
        messages.error(request, 'door not found')
        return redirect('door_list')

    if request.method == 'POST':
        try:
            image = request.FILES.get('image')
            door.head = request.POST.get('head')
            door.description = request.POST.get('description')
            

            # Update the image field
            if image:
                door.image = image

            door.save()
            messages.success(request, 'door edited successfully')
            return redirect('door_list')
        except Exception as e:
            messages.error(request, f'Error editing door: {e}')
            return redirect('door_edit', door_id=door.id) 

    context = {
        'current_page': current_page,
        'door': door
        }
    return render(request, 'admin_app/pages/door_edit.html', context)

@login_required(login_url='/auth/admin/login/')
def door_delete(request, door_id):
    try:
        door = Door.objects.get(id=door_id)
    except Door.DoesNotExist:
        messages.error(request, 'door not found')
        return redirect('door_list')
    
    try: 
        door.delete()
        messages.success(request, 'door deleted successfully')
        return redirect('door_list')
    except Exception as e:
        messages.error(request, f'Error deleting door: {e}')
        return redirect('door_list')






@login_required(login_url='/auth/admin/login/')    
def window_list(request):
    current_page = 'window_list'
    windows = Window.objects.all()
    context = {
        'current_page': current_page,
        'windows': windows
        }
    return render(request, 'admin_app/pages/window_list.html', context)

@login_required(login_url='/auth/admin/login/')
def window_view(request, window_id):
    current_page = 'window_view'
    try:
        window = Window.objects.get(id=window_id)
    except Window.DoesNotExist:
        messages.error(request, 'window not found')
        return redirect('window_list')
    context = {
        'current_page': current_page,
        'window':window
    }
    return render(request, 'admin_app/pages/window_view.html', context)

@login_required(login_url='/auth/admin/login/')
def window_add(request):
    current_page = 'window_add'
    if request.method == 'POST':
        image = request.FILES.get('image') 
        head = request.POST.get('head')
        description = request.POST.get('description')
        
        try:
            window = Window(
                image=image,
                head=head,
                description=description,
            )
            window.save()
            messages.success(request, 'window added successfully')
            return redirect('window_list')
        except Exception as e:
            messages.error(request, f'Error adding window: {e}')
            return redirect('window_add')
        
    context = {
        'current_page': current_page,
    } 
    return render(request, 'admin_app/pages/window_add.html', context)

@login_required(login_url='/auth/admin/login/')
def window_edit(request, window_id):
    current_page = 'window_edit'
    try:
        window = Window.objects.get(id=window_id)
    except Window.DoesNotExist:
        messages.error(request, 'window not found')
        return redirect('window_list')

    if request.method == 'POST':
        try:
            image = request.FILES.get('image')
            window.head = request.POST.get('head')
            window.description = request.POST.get('description')
            

            # Update the image field
            if image:
                window.image = image

            window.save()
            messages.success(request, 'window edited successfully')
            return redirect('window_list')
        except Exception as e:
            messages.error(request, f'Error editing window: {e}')
            return redirect('window_edit', window_id=window.id) 

    context = {
        'current_page': current_page,
        'window': window
        }
    return render(request, 'admin_app/pages/window_edit.html', context)

@login_required(login_url='/auth/admin/login/')
def window_delete(request, window_id):
    try:
        window = Window.objects.get(id=window_id)
    except Window.DoesNotExist:
        messages.error(request, 'window not found')
        return redirect('window_list')
    
    try: 
        window.delete()
        messages.success(request, 'window deleted successfully')
        return redirect('window_list')
    except Exception as e:
        messages.error(request, f'Error deleting window: {e}')
        return redirect('window_list')
    
    
    
    
    

@login_required(login_url='/auth/admin/login/')
def project_list(request):
    current_page = 'project_list'
    projects = Project.objects.all()
    context = {
        'current_page': current_page,
        'projects': projects
        }
    return render(request, 'admin_app/pages/project_list.html', context)

@login_required(login_url='/auth/admin/login/')
def project_view(request, project_id):
    current_page = 'project_view'
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        messages.error(request, 'Project not found')
        return redirect('project_list')
    context = {
        'current_page': current_page,
        'project':project
    }
    return render(request, 'admin_app/pages/project_view.html', context)

@login_required(login_url='/auth/admin/login/')
def project_add(request):
    current_page = 'project_add'
    if request.method == 'POST':
        image = request.FILES.get('image') 
        head = request.POST.get('head')
        description = request.POST.get('description')
        # status = request.POST.get('status') == 'on'
        try:
            project = Project(
                image=image,
                head=head,
                description=description,
                status=True,
            )
            project.save()
            messages.success(request, 'Project added successfully')
            return redirect('project_list')
        except Exception as e:
            messages.error(request, f'Error adding project: {e}')
            return redirect('project_add')
        
    context = {
        'current_page': current_page,
    } 
    return render(request, 'admin_app/pages/project_add.html', context)

@login_required(login_url='/auth/admin/login/')
def project_edit(request, project_id):
    current_page = 'project_edit'
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        messages.error(request, 'Project not found')
        return redirect('project_list')

    if request.method == 'POST':
        try:
            image = request.FILES.get('image')
            project.head = request.POST.get('head')
            project.description = request.POST.get('description')
            # project.status = request.POST.get('status') == 'on'

            # Update the image field
            if image:
                project.image = image

            project.save()
            messages.success(request, 'Project edited successfully')
            return redirect('project_list')
        except Exception as e:
            messages.error(request, f'Error editing project: {e}')
            return redirect('project_edit', project_id=project.id) 

    context = {
        'current_page': current_page,
        'project': project
        }
    return render(request, 'admin_app/pages/project_edit.html', context)

@login_required(login_url='/auth/admin/login/')
def project_delete(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        messages.error(request, 'Project not found')
        return redirect('project_list')
    
    try: 
        project.delete()
        messages.success(request, 'Project deleted successfully')
        return redirect('project_list')
    except Exception as e:
        messages.error(request, f'Error deleting project: {e}')
        return redirect('project_list')
    