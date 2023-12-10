from django.shortcuts import render, redirect
from .models import Profile , Skill 
from django.db.models import Q
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage

def profilesPagination(request, profiles , results):
    page = request.GET.get('page')
    paginator = Paginator(profiles , results)
    
    try:
        profiles = paginator.page(page) 
    except PageNotAnInteger:
        page =1 
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages    
        profiles = paginator.page(page)
        
    left_Index = (int(page) - 5)
    
    if left_Index <1 :
        left_Index =1
        
    right_Index = (int(page) + 5)
    
    if right_Index > paginator.num_pages :
        right_Index = paginator.num_pages
    
    custom_range = range(left_Index, right_Index)
    
    return custom_range , profiles 

def searchProfiles(request):
    search_query = ''
    
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    print(search_query)
    skills = Skill.objects.filter(skill_name__icontains=search_query)
    profiles = Profile.objects.distinct().filter(
            Q(name__icontains=search_query) |
            Q(short_intro__icontains=search_query) |
            Q(skill__in = skills) 
        )
    
    return profiles , search_query 