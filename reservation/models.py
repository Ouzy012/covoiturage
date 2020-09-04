from django.db import models
from django.contrib.auth.models import User


#class Personne(models.Model):
    #prenom = models.CharField(max_length=100)
    #nom = models.CharField(max_length=100)

    #def __str__(self):
        #return self.prenom + " " + self.nom


class Passager(models.Model):
    passager = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.passager)


class Trajet(models.Model):
    depart = models.CharField(max_length=150)
    arrivee = models.CharField(max_length=150)
    prix = models.FloatField()

    def __str__(self):
        return self.depart + " - " + self.arrivee


class Voyage(models.Model):
    passager_fk = models.ForeignKey(User, on_delete=models.CASCADE)
    trajet = models.ForeignKey(Trajet, on_delete=models.CASCADE)


class Conducteur(models.Model):
    conducteur = models.ForeignKey(User, on_delete=models.CASCADE)
    trajet = models.ForeignKey(Trajet, on_delete=models.CASCADE)
    nbre_place = models.IntegerField()
    image_car = models.ImageField(upload_to='images_car', blank=True)

    def __str__(self):
        return str(self.conducteur)

