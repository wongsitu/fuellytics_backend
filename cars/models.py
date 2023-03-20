from django.db import models


class Car(models.Model):
    make = models.CharField(max_length=250, blank=False)
    model = models.CharField(max_length=250, blank=False)
    displacement = models.DecimalField(
        blank=False, decimal_places=6, max_digits=10)
    year = models.PositiveIntegerField(blank=False)
    is_supercharged = models.BooleanField(blank=False, default=False)
    drag = models.DecimalField(blank=False, decimal_places=6, max_digits=10)
    image_url = models.ImageField(
        upload_to='cars', blank=True, name="image_url")

    def __format__(self):
        return self.model
