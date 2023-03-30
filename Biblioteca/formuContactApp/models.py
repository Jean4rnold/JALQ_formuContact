from django.db import models

# Create your models here.
class contacto(models.Model):
    codigo = models.CharField(max_length=45, null=False)
    nombre = models.CharField(max_length=150, null=False)
    apellidos = models.CharField(max_length=150, null=False)
    email = models.CharField(max_length=150, null=False)
    telefono = models.CharField(max_length=10, null=False)
    mensaje = models.CharField(max_length=500, null=False)
    estado = models.CharField(max_length=150, null=False)
