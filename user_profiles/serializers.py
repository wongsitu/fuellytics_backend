from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, profile):
        user = User.objects.get(id=profile.user.id)
        serializer = UserSerializer(instance=user)
        return serializer.data

    class Meta:
        model = UserProfile
        fields = "__all__"
