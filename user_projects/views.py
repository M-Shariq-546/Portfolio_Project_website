from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm

def projects(request):
    projectList = Project.objects.all()
    
    context = {
        'projects':projectList,
        'title':"Place to Connect Developers",
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
    form = ProjectForm()
    
    if request.method=='POST':
        form = ProjectForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {
        'form':form,
        'title':"Create Project",
    }
    return render(request, 'projects/project_form.html', context)


@login_required(login_url='login')
def updateProject(request , pk):
    project = Project.objects.get(pk=pk)
    form = ProjectForm(instance = project)

    if request.method=='POST':
        form = ProjectForm(request.POST, request.FILES, instance = project)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {
        'form':form,
        'title':"Update Project",
    }
    return render(request, 'projects/project_form.html', context)



@login_required(login_url='login')
def deleteProject(request , pk):
    project = Project.objects.get(pk=pk)
    if request.method == "POST":
        project.delete()
        return redirect('home')
    
    context = {
        'project':project,
        'title':"Delete Project",
    }
    return render(request , 'projects/delete_project.html' , context)
# Create your views here.
