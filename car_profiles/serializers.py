from car_profiles.models import CarProfile
from user_profiles.models import UserProfile
from cars.models import Car
from django.contrib.auth.models import User
from rest_framework import serializers
from user_profiles.serializers import UserProfileSerializer
from cars.serializers import CarSerializer

class CarProfileSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    user = serializers.SerializerMethodField()
    car = serializers.SerializerMethodField()

    def get_user(self, profile):
        user = UserProfile.objects.get(user__id=profile.user.id)
        serializer = UserProfileSerializer(instance=user)
        return serializer.data

    def get_car(self, profile):
        car = Car.objects.get(id=profile.car.id)
        serializer = CarSerializer(instance=car)
        return serializer.data

    class Meta:
        model = CarProfile
        fields = ('id', 'user', 'car', 'image_url')
