from cars.models import Car
from rest_framework import viewsets, filters
from cars.serializers import CarSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class Cars(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CarSerializer
    queryset = Car.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['make', 'model',
                     'displacement', 'year', 'is_supercharged', 'drag']
