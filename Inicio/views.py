from django.shortcuts import render
from django.http import HttpResponse
from .models import Pelicula 

def Inicio(request):
    return render(request, 'inicio.html')

def nueva(request):
     return render(request, 'nueva.html')


def crear_pelicula (request, pelicula, genero):
    
    nueva_pelicula = Pelicula(pelicula=pelicula, genero=genero)
    nueva_pelicula.save()
    return render(request, 'crear_pelicula.html', {'pelicula_guardada': pelicula})

