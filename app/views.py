from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect

from .models import Personne
from .forms import TrajetForm


def index(request):
    liste_personne = Personne
    template = loader.get_template('app/index.html')
    context = {
        'liste_personne': liste_personne,
    }
    return HttpResponse(template.render(context, request))

def create_voyage(request):
    form = TrajetForm()
    if request.method == 'POST':
        form = TrajetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'app/create_voyage.html', context)