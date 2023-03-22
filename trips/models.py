from django.db import models
from user_profiles.models import UserProfile
from car_profiles.models import CarProfile
from django.contrib.postgres.fields import ArrayField


class Trip(models.Model):
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()
    route_coordinates = ArrayField(ArrayField(models.IntegerField(), size=2))
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='user_profile')
    car_profile = models.ForeignKey(
        CarProfile, on_delete=models.CASCADE, related_name='car_profile')
    fuel_consumption = models.DecimalField(
        decimal_places=3, max_digits=10, default=0.0)
    fuel_consumption_price = models.DecimalField(
        decimal_places=3, max_digits=10, default=0.0)
    co2_emissions = models.DecimalField(
        decimal_places=3, max_digits=10, default=0.0)
    n2o_emissions = models.DecimalField(
        decimal_places=3, max_digits=10, default=0.0)
    ch4_emissions = models.DecimalField(
        decimal_places=3, max_digits=10, default=0.0)

    def __str__(self):
        return self.model
