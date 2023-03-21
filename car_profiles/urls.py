from django.urls import path
from . import views

urlpatterns = [
    path('car_profiles', views.CarProfiles.as_view())
]
