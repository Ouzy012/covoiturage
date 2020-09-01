from django.db import models

class Personne(models.Model):
    personne_id = models.AutoField(primary_key=True)
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=30)