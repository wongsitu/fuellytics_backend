from cars.models import Car
from rest_framework import viewsets, filters
from cars.serializers import CarSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from cars.forms import CarForm
from rest_framework.response import Response
from django.forms.models import model_to_dict

class Cars(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CarSerializer
    queryset = Car.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['make', 'model',
                     'displacement', 'year', 'is_supercharged', 'drag']

    def create(self, request):
        car_form = CarForm(request.data)

        if car_form.is_valid():
            if 'image_url' in request.FILES:
                new_car = car_form.save()
            else:
                new_car = car_form.save(commit=False)
                new_car.image_url = None
                new_car.save()

            return Response({'success': True, 'data': model_to_dict(new_car)})
        else:
            return Response({'success': False, 'errors': car_form.errors})
