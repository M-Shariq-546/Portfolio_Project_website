from django.urls import path, include
from . import views
urlpatterns = [
    path('' , views.getRoutes),
    path('projects/' ,views.getProjects),
    path('project/<str:pk>' ,views.getProject),
]
