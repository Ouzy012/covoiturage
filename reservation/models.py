from django.db import models

class Personne(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)

    #def __str__(self):
        #return self.prenom + " " + self.nom


class Passager(models.Model):
    passager = models.ForeignKey(Personne, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.passager)


class Trajet(models.Model):
    depart = models.CharField(max_length=150)
    arrivee = models.CharField(max_length=150)
    prix = models.FloatField()

    #def __str__(self):
        #return self.depart + " " + self.arrivee + " " + str(self.prix)


class Voyage(models.Model):
    passager_fk = models.ForeignKey(Passager, on_delete=models.CASCADE)
    trajet = models.ForeignKey(Trajet, on_delete=models.CASCADE)


class Conducteur(models.Model):
    conducteur = models.ForeignKey(Personne, on_delete=models.CASCADE)
    trajet = models.ForeignKey(Trajet, on_delete=models.CASCADE)
    nbre_place = models.IntegerField()
    image_vehicule = models.CharField(max_length=100)

    def __str__(self):
        return str(self.conducteur)

