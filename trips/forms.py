from django import forms
from trips.models import Trip
import jsonschema
import json

route_coordinates_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "accuracy": {"type": ["number", "null"], "nullable": True},
            "altitude": {"type": ["number", "null"], "nullable": True},
            "altitudeAccuracy": {"type": ["number", "null"], "nullable": True},
            "heading": {"type": ["number", "null"], "nullable": True},
            "latitude": {"type": "number"},
            "longitude": {"type": "number"},
            "speed": {"type": ["number", "null"], "nullable": True}
        },
        "required": ["latitude", "longitude"]
    }
}

class RouteCoordinatesListField(forms.Field):
    default_error_messages = {
        'invalid': 'Invalid JSON format.',
        'validation_failed': 'Validation failed: %(error)s',
    }

    def __init__(self, **kwargs):
        self.schema = kwargs.pop('schema', None)
        super().__init__(**kwargs)

    def to_python(self, value):
        if value in self.empty_values:
            return []

        try:
            if isinstance(value, list):
                jsonschema.validate(instance=value, schema=self.schema)
                return value
            else:
                value = json.loads(value)
                jsonschema.validate(instance=value, schema=self.schema)
                return value
        except (ValueError, TypeError, jsonschema.ValidationError) as e:
            raise forms.ValidationError(
                self.error_messages['validation_failed'] % {'error': str(e)}
            )

    def prepare_value(self, value):
        if value is None:
            return ''
        elif isinstance(value, list):
            return json.dumps(value)
        else:
            return value


class TripsForm(forms.ModelForm):
    car_profile_id = forms.CharField(required=True)
    route_coordinates = RouteCoordinatesListField(
        schema=route_coordinates_schema,
        label='Route coordinates',
        help_text='Enter a list of coordinates as JSON.'
    )
    started_at = forms.CharField(required=True)
    ended_at = forms.CharField(required=True)

    class Meta():
        model = Trip
        fields = ['car_profile_id', 'route_coordinates', 'ended_at', 'started_at']
