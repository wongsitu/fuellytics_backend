from django import forms
from cars.models import Car


class CarForm(forms.ModelForm):
    image_url = forms.ImageField(required=False)

    class Meta():
        model = Car
        fields = ['make', 'model', 'displacement', 'year', 'is_supercharged', 'drag']