from django.contrib import admin

from .models import Personne, Conducteur, Passager, Trajet, Voyage

admin.site.register(Personne)
admin.site.register(Conducteur)
admin.site.register(Passager)
admin.site.register(Trajet)
admin.site.register(Voyage) 