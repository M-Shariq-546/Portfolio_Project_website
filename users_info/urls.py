from django.urls import path
from . import views
urlpatterns = [
    path('', views.profiles , name='users_profiles'),
    path('profile/<str:pk>/', views.single_profile , name='profile'),
    path('login/' , views.Login , name='login'),
    path('logout/' , views.Logout , name='logout'),
    path('register/' , views.registerUser , name='register'),
    path('account/' , views.userAccount , name='account'),
    path('update_account_info/' , views.userUpdate , name='update_account'),
    path('create_skill/' , views.createSkill , name='addskills'),
    path('update_skill/<str:pk>' , views.updateSkill , name='update_skills'),
    path('delete_skill/<str:pk>' , views.deleteSkill , name='delete_skills'),
]
