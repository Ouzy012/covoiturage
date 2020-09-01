from django.contrib import admin

from .models import Personne, Conducteur, Passager, Trajet

admin.site.register(Personne)
admin.site.register(Conducteur)
admin.site.register(Passager)
admin.site.register(Trajet)