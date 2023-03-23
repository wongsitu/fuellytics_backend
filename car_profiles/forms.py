from django import forms
from car_profiles.models import CarProfile


class CarProfileForm(forms.ModelForm):
    car_id = forms.CharField(required=True)

    class Meta():
        model = CarProfile
        fields = ('car_id', 'image_url')
