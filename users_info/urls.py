from django.urls import path
from . import views
urlpatterns = [
    path('', views.profiles , name='users_profiles'),
    path('profile/<str:pk>/', views.single_profile , name='profile'),
    path('login/' , views.Login , name='login'),
    path('logout/' , views.Logout , name='logout'),
    path('register/' , views.registerUser , name='register'),
]
