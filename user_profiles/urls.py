from .views import UserProfile
from django.urls import path

urlpatterns = [
    path('api/users/<int:pk>/', UserProfile.as_view())
]
