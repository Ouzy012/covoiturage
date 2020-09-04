from django.forms import ModelForm
from django import forms
from .models import Conducteur, Trajet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TrajetForm(ModelForm):
    class Meta:
        model = Trajet
        fields = '__all__'

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
	    model = User
	    fields = ["username", "email", "password1", "password2"]

class VoyageForm(ModelForm):
    class Meta:
        model = Conducteur
        fields = '__all__'