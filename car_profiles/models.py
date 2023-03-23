from django.db import models
from cars.models import Car
from django.contrib.auth.models import User


class CarProfile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    car = models.ForeignKey(
        Car, on_delete=models.CASCADE, related_name='car')
    image_url = models.ImageField(
        upload_to='car_profiles', blank=True)

    def __str__(self):
        return f'''{self.car.model} by {self.user.username}'''
