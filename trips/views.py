from trips.models import Trip
from rest_framework import viewsets, filters
from trips.serializers import TripSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class Trips(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TripSerializer
    queryset = Trip.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend]
