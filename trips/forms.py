from django import forms
from trips.models import Trip

class TripsForm(forms.ModelForm):
    car_profile_id = forms.CharField(required=True)

    class Meta():
        model = Trip
        fields = ['started_at', 'ended_at', 'fuel_consumption', 'co2_emissions', 'n2o_emissions', 'ch4_emissions', 'car_profile_id']
