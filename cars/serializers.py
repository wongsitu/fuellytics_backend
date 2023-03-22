from .models import Car
from rest_framework import serializers

class CarSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    
    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'displacement',
                  'year', 'is_supercharged', 'drag', 'image_url']
