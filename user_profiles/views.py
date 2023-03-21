from user_profiles.models import UserProfile
from django.contrib.auth.models import User
from rest_framework import viewsets, mixins
from user_profiles.serializers import UserProfileSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404


class UserProfiles(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = UserProfileSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None):
        user = get_object_or_404(User, id=self.kwargs['pk'])
        user_profile, created = UserProfile.objects.get_or_create(
            user=user)
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data)
