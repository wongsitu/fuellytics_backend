from .models import Car
from rest_framework import serializers

class CarSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Car
        fields = ['id', 'isbn', 'title', 'author', 'year']