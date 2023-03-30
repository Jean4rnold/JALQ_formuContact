from django.contrib import admin
from django.urls import path

from Biblioteca.views import inicio, contact
from librosApp.views import crearLibro
from formuContactApp.views import crearContacto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('Contact/', contact),
    path('clibro/', crearLibro),
    path('cContacto/', crearContacto),
]
