from django.db import models
from user_profiles.models import UserProfile
from car_profiles.models import CarProfile
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields.jsonb import JSONField as JSONBField

class Trip(models.Model):
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()
    route_coordinates = models.JSONField(default=list)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='user_profile')
    car_profile = models.ForeignKey(
        CarProfile, on_delete=models.CASCADE, related_name='car_profile')
    fuel_consumption = models.DecimalField(
        decimal_places=3, max_digits=10, default=0.0)
    average_speed = models.DecimalField(
        decimal_places=3, max_digits=10, default=0.0)
    co2_emissions = models.DecimalField(
        decimal_places=3, max_digits=10, default=0.0)

    def __str__(self):
        return self.user_profile.user.username
