from trips.models import Trip
from rest_framework import viewsets, filters
from trips.serializers import TripSerializer
from trips.forms import TripsForm
from car_profiles.forms import CarProfile
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class Trips(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TripSerializer
    queryset = Trip.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend]

    def create(self, request):
        trip_form = TripsForm(data=request.data)

        if trip_form.is_valid():
            new_trip = trip_form.save(commit=False)
            car_profile_id = request.data.get('car_profile_id')
            car_profile = get_object_or_404(CarProfile, id=car_profile_id)
            new_trip.user = request.user
            new_trip.car_profile = car_profile
            new_trip.save()

            return Response({'success': True, 'data': TripSerializer(new_trip).data})
        else:
            return Response({'success': False, 'errors': trip_form.errors})
