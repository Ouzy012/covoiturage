from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("", views.home, name="home"),
    path("create_voyage/", views.create_voyage, name="index"),
    path("register/", views.register, name="register"),
    path("reserver/<int:trajet_id>", views.reserver, name="reserver")
]