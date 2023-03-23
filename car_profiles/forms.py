from django import forms
from car_profiles.models import CarProfile


class CarForm(forms.ModelForm):
    car_id = forms.CharField(required=True)
    image_url = forms.FileField(required=False)

    class Meta():
        model = CarProfile
        fields = ('car_id', 'image_url')
