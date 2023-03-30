from django.contrib import admin
from formuContactApp.models import contacto

# Register your models here.
class contactoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'apellidos','email','telefono','mensaje','estado')

admin.site.register(contacto, contactoAdmin)
