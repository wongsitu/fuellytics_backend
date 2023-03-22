from car_profiles.models import CarProfile
from cars.models import Car
from django.contrib.auth.models import User
from rest_framework import serializers
from accounts.serializers import UserSerializer
from cars.serializers import CarSerializer

class CarProfileSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    user = serializers.SerializerMethodField()
    car = serializers.SerializerMethodField()

    def get_user(self, profile):
        user = User.objects.get(id=profile.user.id)
        serializer = UserSerializer(instance=user)
        return serializer.data

    def get_car(self, profile):
        car = Car.objects.get(id=profile.car.id)
        serializer = CarSerializer(instance=car)
        return serializer.data

    class Meta:
        model = CarProfile
        fields = ['id', 'user', 'car', 'image_url']
