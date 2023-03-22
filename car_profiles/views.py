from .models import CarProfile

from rest_framework import viewsets, filters
from car_profiles.serializers import CarProfileSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.forms.models import model_to_dict


class CarProfiles(viewsets.ModelViewSet):
    queryset = CarProfile.objects.all().order_by('id')
    serializer_class = CarProfileSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['user__email', 'user__firstname',
                     'user__lastname', 'car__make', 'car__model',
                     'car__year', 'car__displacement', 'car__drag']
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
