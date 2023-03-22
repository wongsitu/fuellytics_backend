from trips.models import Trip
from rest_framework import serializers

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = "__all__"