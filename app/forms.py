from django.forms import ModelForm
from .models import Personne, Conducteur, Trajet


class TrajetForm(ModelForm):
    class Meta:
        model = Trajet
        fields = '__all__'