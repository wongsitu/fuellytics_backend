# chat/routing.py
from django.urls import re_path

from . import consumers

ws_urlpatterns = [
    re_path("ws/mechanization",
            consumers.MechanizationConsumer.as_asgi()),
]
