from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_voyage/', views.create_voyage, name='create_voyage'),
]