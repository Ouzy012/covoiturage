from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from reservation.models import Personne, Trajet
from .forms import TrajetForm, RegisterForm

def index(response):
	listeP = Personne.objects.all()
	return render(response, "reservation/liste_personnes.html", {"listeP":listeP})

def home(response):
	listeV = Trajet.objects.all()
	user_id = response.user.id
	return render(response, "reservation/home.html", {'listeV':listeV, 'user_id':user_id})

def reserver(response, voyage_id):
	print(response.method)

def create_voyage(response):
	form = TrajetForm()
	context = {'form': form}
	if response.method == "POST":
		form = TrajetForm(response.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/index/")
	else:
		form = TrajetForm()

	return render(response, "reservation/create_voyage.html", context)

def register(response):
	if response.method == "POST":
		form = RegisterForm(response.POST)
		if form.is_valid():
			form.save()
			return redirect("/index/")
	else:
		form = RegisterForm()

	return render(response, "registration/register.html", {"form":form})