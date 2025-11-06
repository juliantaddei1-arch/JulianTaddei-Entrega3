from django.shortcuts import render
from django.http import HttpResponse

def Inicio(request):
    #return HttpResponse ('Soy el proyecto')
    return render(request, 'inicio.html')

def nueva(request):
    #return HttpResponse ('Soy el proyecto')
    return render(request, 'nueva.html')

