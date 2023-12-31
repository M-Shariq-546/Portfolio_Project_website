from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('' , views.getRoutes),
    path('projects/' ,views.getProjects),
    path('project/<str:pk>' ,views.getProject),
    path('remove-tag/' ,views.removeTag),
    path('project/<str:pk>/vote' ,views.getProjectVote),
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
