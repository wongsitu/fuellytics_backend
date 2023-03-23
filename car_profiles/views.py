from car_profiles.models import CarProfile
from cars.models import Car
from car_profiles.forms import CarProfileForm

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

    def create(self, request):
        car_form = CarProfileForm(request.data, request.FILES)

        if car_form.is_valid():
            new_car_profile = car_form.save(commit=False)
            car_id = request.data.get('car_id')
            car = Car.objects.get(id=car_id)
            new_car_profile.user = request.user
            new_car_profile.car = car
            new_car_profile.save()
            return Response({'success': True, 'data': model_to_dict(new_car_profile)})
        else:
            return Response({'success': False, 'errors': car_form.errors})
