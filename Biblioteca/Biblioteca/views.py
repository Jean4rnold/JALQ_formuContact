from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
    return render(request, "inicio.html")

def contacto(request):
    return render(request, "contacto.html")