from django.db import models
from django.contrib.auth.models import User

# Userprofile
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    profile_image = models.ImageField(upload_to='photos', blank=True, name="profile_image")
    first_name = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.user.username