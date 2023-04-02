from trips.models import Trip
from rest_framework import viewsets, filters
from trips.serializers import TripSerializer
from trips.forms import TripsForm
from car_profiles.forms import CarProfile
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from trips.filters import TripFilter
from user_profiles.models import UserProfile
from rest_framework.response import Response
import datetime

class Trips(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TripSerializer
    queryset = Trip.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend]
    filter_class = TripFilter

    def create(self, request):
        trip_form = TripsForm(data=request.data)

        if trip_form.is_valid():
            new_trip = trip_form.save(commit=False)
            started_at = request.data.get('started_at')
            ended_at = request.data.get('ended_at')
            date_format = "%Y-%m-%dT%H:%M:%SZ"

            formatted_started_at = datetime.datetime.strptime(started_at, date_format)
            formatted_ended_at = datetime.datetime.strptime(ended_at, date_format)

            new_trip.started_at = formatted_started_at
            new_trip.ended_at = formatted_ended_at

            user_profile, created = UserProfile.objects.get_or_create(user=request.user)
            new_trip.user_profile = user_profile

            car_profile_id = request.data.get('car_profile_id')
            car_profile = get_object_or_404(CarProfile, id=car_profile_id)
            new_trip.car_profile = car_profile
            new_trip.save()

            return Response({'success': True, 'data': TripSerializer(new_trip).data})
        else:
            return Response({'success': False, 'errors': trip_form.errors})
