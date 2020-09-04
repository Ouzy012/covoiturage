from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from reservation.models import Trajet, Conducteur, Voyage, Passager
from .forms import TrajetForm, RegisterForm, VoyageForm


def index(response):
	listeV = Conducteur.objects.all()
	user_id = response.user.id
	context = {'listeV': listeV, 'user_id':user_id}
	return render(response, "reservation/liste_voyages.html", context)

def infos_voyage(response, pk):
	showImg = Conducteur.objects.filter(pk=pk)
	context = {'img': showImg}
	print(showImg)
	return render(response, "reservation/infos_voyage.html", context)

def home(response):
	listeT = Trajet.objects.all()
	user_id = response.user.id
	context = {'listeT':listeT, 'user_id':user_id}
	return render(response, "reservation/home.html", context)

def create_new_voyage(response):
	form = VoyageForm()
	user_id = response.user.id
	context = {'form': form, 'user_id':user_id}
	if response.method == "POST":
		form = VoyageForm(response.POST)
		if form.is_valid():
			form.save()	
			return HttpResponseRedirect("/index/")
		else:
			form = VoyageForm()

	return render(response, "reservation/create_new_voyage.html", context)

def reserver(response, trajet_id, passager_id, conducteur_id):
	#if response.method == "GET":
	voyage = Voyage(passager_fk_id=passager_id, trajet_id=trajet_id)
	voyage.save()

	voir_conducteur = Conducteur.objects.get(conducteur_id=conducteur_id)
	voir_conducteur.nbre_place -= 1
	voir_conducteur.save()
	
	return HttpResponseRedirect("/index/")

def create_voyage(response):
	form = TrajetForm()
	context = {'form': form}
	if response.method == "POST":
		form = TrajetForm(response.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/")
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
