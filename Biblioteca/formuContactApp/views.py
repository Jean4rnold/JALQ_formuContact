from django.shortcuts import render
from formuContactApp.models import contacto

# Create your views here.
def crearContacto(request):
    if request.method == 'POST':
        Codigo = request.POST['codigo']
        Nombre = request.POST['nombre']
        Apellidos = request.POST['apellidos']
        Email = request.POST['email']
        Telefono = request.POST['telefono']
        Mensaje = request.POST['mensaje']
        Estado = request.POST['estado']

        newContacto = contacto(codigo=Codigo, nombre=Nombre, apellidos=Apellidos, email=Email, telefono=Telefono,mensaje=Mensaje, estado=Estado)
        newContacto.save()

        return render(request, "crearContacto.html", {"nombre": Nombre})
    return render(request, "crearContacto.html")
