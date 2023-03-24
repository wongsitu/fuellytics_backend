from cars.models import Car
from rest_framework import viewsets, filters
from cars.serializers import CarSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from cars.forms import CarForm
from rest_framework.response import Response

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
            new_car = car_form.save(commit=False)
            new_car.image_url = request.FILES.get('image_url', None)

            if 'image_url' in request.FILES:
                new_car.image_url = request.FILES['image_url']
            new_car.save()
            return Response({'success': True, 'data': CarSerializer(new_car).data })
        else:
            return Response({'success': False, 'errors': car_form.errors})
