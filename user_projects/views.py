from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm
from .utils import searchProjects , projectsPagination
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage

def projects(request):
    projects , search_query = searchProjects(request)
    #projectList = Project.objects.all()    
    results = 3
    custom_range , projects = projectsPagination(request, projects , results)
    context = {
        'projects':projects,
        'title':"Place to Connect Developers",
        'search_query':search_query,
        'custom_range':custom_range,
    }
    return render(request , 'projects/user_projects.html' , context)


def single_project(request , pk):
    project_info = Project.objects.get(pk=pk)
    ProObj = project_info.tag.all()
    context ={
        "project":project_info,
        "tags":ProObj,
        'title':"Project Details",
    }
    return render(request , 'projects/single_project.html' , context)

# CRUD Operation
@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    
    if request.method=='POST':
        form = ProjectForm(request.POST , request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            messages.success(request , "New Project Created successfully!")
            return redirect('account')
    
    context = {
        'form':form,
        'title':"Create Project",
    }
    return render(request, 'projects/project_form.html', context)


@login_required(login_url='login')
def updateProject(request , pk):
    profile = request.user.profile
    project = profile.project_set.get(pk=pk)
    form = ProjectForm(instance = project)

    if request.method=='POST':
        form = ProjectForm(request.POST, request.FILES, instance = project)
        if form.is_valid():
            form.save()
            messages.success(request , "Project Updated successfully!")
            return redirect('account')
    
    context = {
        'form':form,
        'title':"Update Project",
    }
    return render(request, 'projects/project_form.html', context)



@login_required(login_url='login')
def deleteProject(request , pk):
    profile = request.user.profile
    project = profile.project_set.get(pk=pk)
    if request.method == "POST":
        project.delete()
        messages.success(request , "Project Deleted successfully!")
        return redirect('account')
    
    context = {
        'project':project,
        'title':"Delete Project",
    }
    return render(request , 'projects/delete_project.html' , context)
# Create your views here.
