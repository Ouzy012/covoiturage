from django.contrib import admin


from .models import Conducteur, Passager, Trajet, Voyage

admin.site.register(Conducteur)
admin.site.register(Passager)
admin.site.register(Trajet)
admin.site.register(Voyage) 
