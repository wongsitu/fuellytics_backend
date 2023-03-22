from django.db import models
from user_profiles.models import UserProfile

class Trip(models.Model):
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()
    route_coordinates = ArrayField(ArrayField(models.IntegerField(size=2)))
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='user')
        
    def __str__(self):
        return self.model