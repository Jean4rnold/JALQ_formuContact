from django.contrib import admin
from librosApp.models import libro
#from librosApp.models import libro, usuario_data
# Register your models here.
class libroAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'titulo', 'autor','genero','estado')

#class usuario_dataAdmin(admin.ModelAdmin):
 #   list_display = ('fechaNacimiento', 'Genero', 'idUser')

admin.site.register(libro, libroAdmin)
#admin.site.register(usuario_Data, usuario_dataAdmin)