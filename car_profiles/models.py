from django.db import models
from cars.models import Car
from django.contrib.auth.models import User
# Create your models here.


class CarProfile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    car = models.ForeignKey(
        Car, on_delete=models.CASCADE, related_name='car')
    image_url = models.ImageField(
        upload_to='car_profiles', blank=True, name="image_url")

    def __format__(self):
        return self.car
