from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login , authenticate , logout
from .models import Profile
from user_projects.models import Project
def profiles(request):
    profiles = Profile.objects.all()
    context ={
        'profiles':profiles,
        'title':"Developers Page",
    }
    return render(request , "users/profiles.html" , context)

def single_profile(request , pk):
    user_profile = Profile.objects.get(id=pk)
    topskills = user_profile.skill_set.exclude(skill_description__exact="")
    otherskills = user_profile.skill_set.filter(skill_description="")
    projects = Project.objects.all()    
    
    context ={
        'projects':projects,
        'user_profile':user_profile,
        'skills':topskills,
        'otherskills':otherskills,
        'title':"Developer Info",
    }
    
    return render(request, "users/user-profile.html" , context)

def Login(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, " username does not exists ! ")
        
        user = authenticate(request , username=username , password=password)
        
        if user is not None:
            login(request , user)
            messages.success(request, " user Successfully logged out ! ")
            return redirect("home")
        else:
            messages.warning(request , "Username or Password is incorrect ! Please try again ")        
    return render(request , 'users/login_register.html')

def Logout(request):
    logout(request)
    return redirect('login')



# Create your views here.
