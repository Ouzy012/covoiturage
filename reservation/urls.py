from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("", views.home, name="home"),
    path("create_voyage/", views.create_voyage, name="index"),
    path("register/", views.register, name="register"),
    path("reserver/<int:trajet_id>/<int:passager_id>/<int:conducteur_id>", views.reserver, name="reserver"),
    path("create_new_voyage/", views.create_new_voyage, name="create_new_voyage"),
    path("infos_voyage/<int:pk>", views.infos_voyage, name="infos_voyage"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)