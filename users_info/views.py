from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm , ProfileForm , SkillForm
from django.contrib.auth import login , authenticate , logout
from .models import Profile
from user_projects.models import Project 
import profile
from .utils import searchProfiles, profilesPagination



def profiles(request):
    profiles , search_query = searchProfiles(request)
    #profiles = Profile.objects.all()
    results = 2
    custom_range , profiles = profilesPagination(request, profiles , results)
    context ={
        'profiles':profiles,
        'title':"Developers Page",
        'search_query':search_query,
        'custom_range':custom_range,
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


@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()
    context ={
        'profile':profile,
        'skills':skills,
        'projects':projects,
    }
    return render(request , 'users/account.html' , context)



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
            return redirect('update_account')
        else:
            messages.error(request , "An Error Occurred Please Try Again")
    page = 'register'
    context ={
        'page':page,
        'form':form
    }
    return render(request, "users/login_register.html" , context)

@login_required(login_url='login')
def userUpdate(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method=="POST":
        form = ProfileForm(request.POST , request.FILES , instance = profile)
        if form.is_valid():
            form.save()
            messages.success(request , "Profile Updated successfully!")
            return redirect('account')
    context = {
        'form':form,
    }
    return render(request, 'users/account_update.html' , context)

@login_required(login_url='login')
def createSkill(request):
    profile = request.user.profile
    form = SkillForm()
    if request.method =='POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, "New Skill Successfully Added")
            return redirect('account')
    context = {
        'form':form
    }
    return render(request , 'users/skill_form.html' , context)


@login_required(login_url='login')
def updateSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)
    if request.method =='POST':
        form = SkillForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Skill Successfully Updated")
            return redirect('account')
    context = {
        'form':form,
        'skill':skill,
    }
    return render(request , 'users/skill_form.html' , context)

@login_required(login_url='login')
def deleteSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)
    if request.method =='POST':
        skill.delete()
        messages.success(request, "Skill Successfully Deleted")
        return redirect('account')
    context = {
        'form':form
    }
    return render(request , 'users/delete_skill.html' , context)


# Create your views here.
