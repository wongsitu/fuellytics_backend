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
from django.shortcuts import get_object_or_404


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
        car_profile_form = CarProfileForm(data=request.data)
        user = self.request.user

        if car_profile_form.is_valid():
            new_car_profile = car_profile_form.save(commit=False)
            car_id = request.data.get('car_id')
            car = get_object_or_404(Car, id=car_id)
            new_car_profile.user = user
            new_car_profile.car = car

            if 'image_url' in request.FILES:
                new_car_profile.image_url = request.FILES['image_url']

            new_car_profile.save()
            return Response({'success': True, 'data': CarProfileSerializer(new_car_profile).data})
        else:
            return Response({'success': False, 'errors': car_profile_form.errors})

    def delete(self, request, pk=None):
        car_profile = get_object_or_404(CarProfile, id=pk)
        car_profile.delete()

        return Response({'success': True, 'data': CarProfileSerializer(car_profile).data})
