from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)

    class Meta():
        model = User
        fields = ('password','email', 'username')