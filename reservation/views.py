from django.shortcuts import render
from reservation.models import Personne

def index(response, id):
	listeP = Personne
	return render(response, "reservation/liste_personnes.html", {"listeP":listeP})

def home(response):
	return render(response, "reservation/home.html", {})