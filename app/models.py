from django.db import models

class Personne(models.Model):
    prenom = models.CharField(max_length=60)
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.prenom + " " + self.nom


class Passager(models.Model):
    passager = models.ForeignKey(Personne, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.passager)


class Trajet(models.Model):
    depart = models.CharField(max_length=100)
    arrivee = models.CharField(max_length=100)
    prix = models.FloatField()

    def __str__(self):
        return self.depart + " " + self.arrivee


class Voyage(models.Model):
    passager = models.ForeignKey(Passager, on_delete=models.CASCADE)
    trajet = models.ForeignKey(Trajet, on_delete=models.CASCADE)


class Conducteur(models.Model):
    conducteur = models.ForeignKey(Personne, on_delete=models.CASCADE)
    trajet = models.ForeignKey(Trajet, on_delete=models.CASCADE)
    nbre_place = models.IntegerField()
    image_vehicule = models.CharField(max_length=100)

    def __str__(self):
        return str(self.conducteur)
