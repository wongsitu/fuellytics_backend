from django.urls import path
from car_profiles.views import CarProfiles

urlpatterns = [
    path('car_profiles/', CarProfiles.as_view())
]
