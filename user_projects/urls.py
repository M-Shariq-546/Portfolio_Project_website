from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='home'),
    path('project/<str:pk>', views.single_project , name='project'),
    path('create_project', views.createProject, name='create_project'),
    path('vote_project', views.voteProject, name='vote_project'),
    path('update_project/<str:pk>', views.updateProject, name='update_project'),
    path('delete_project/<str:pk>', views.deleteProject, name='delete_project'),
]
