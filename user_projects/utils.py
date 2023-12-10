from django.shortcuts import render, redirect
from .models import Project, Tag
from user_projects.models import Project 
from django.db.models import Q
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage

def projectsPagination(request, projects , results):
    page = request.GET.get('page')

    paginator = Paginator(projects , results)
    
    try:
        projects = paginator.page(page) 
    except PageNotAnInteger:
        page =1 
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages    
        projects = paginator.page(page)
        
    left_Index = (int(page) - 5)
    
    if left_Index <1 :
        left_Index =1
        
    right_Index = (int(page) + 5)
    
    if right_Index > paginator.num_pages :
        right_Index = paginator.num_pages
    
    custom_range = range(left_Index, right_Index)
    
    return custom_range , projects  
    

def searchProjects(request):
    search_query = ''
    
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    print(search_query)
    tag = Tag.objects.filter(name__icontains=search_query)
    projects = Project.objects.distinct().filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(owner__name__icontains=search_query) |
            Q(tag__in = tag) 
        )
    
    return projects , search_query 