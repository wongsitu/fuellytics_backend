from trips.views import Trips
from django.urls import path

urlpatterns = [
    path('trips/', Trips.as_view())
]