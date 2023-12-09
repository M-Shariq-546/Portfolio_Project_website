from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm
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
    page = 'login'
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
            messages.success(request, " You are Successfully log in ! ")
            return redirect("home")
        else:
            messages.error(request , "Username or Password is incorrect ! Please try again ")        
    return render(request , 'users/login_register.html')

def Logout(request):
    logout(request)
    messages.success(request, " You are Successfully log out ! ")
    return redirect('login')

def registerUser(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) # this could save the user but make temporary instance of user
            user.username = user.username.lower()
            user.save()    
            messages.success(request , "User successfully registered!")
            login(request , user)
            return redirect('home')
        else:
            messages.error(request , "An Error Occurred Please Try Again")
    page = 'register'
    context ={
        'page':page,
        'form':form
    }
    return render(request, "users/login_register.html" , context)

# Create your views here.
