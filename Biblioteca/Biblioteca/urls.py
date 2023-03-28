from django.contrib import admin
from django.urls import path
from Biblioteca.views import inicio, contacto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('contacto/', contacto),
]
