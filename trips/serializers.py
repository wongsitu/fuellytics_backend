from trips.models import Trip
from car_profiles.models import CarProfile
from car_profiles.serializers import CarProfileSerializer
from rest_framework import serializers

class TripSerializer(serializers.ModelSerializer):
    car_profile = serializers.SerializerMethodField()

    def get_car_profile(self, trip):
        car_profile = CarProfile.objects.get(id=trip.car_profile.id)
        serializer = CarProfileSerializer(instance=car_profile)
        return serializer.data

    class Meta:
        model = Trip
        fields = "__all__"