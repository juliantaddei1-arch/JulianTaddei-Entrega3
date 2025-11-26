from django.shortcuts import render, redirect
from django.http import HttpResponse
from Inicio.models import Pelicula
from .forms import BusquedaPeliculaForm
from Inicio.forms import CrearPelicula
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import UpdateView, DeleteView




def actualizar_pelicula(request, id):
    pelicula = Pelicula.objects.get(id=id)

    if request.method == "POST":
        formulario = CrearPelicula(request.POST)

        if formulario.is_valid():
            pelicula.genero = formulario.cleaned_data['genero']
            pelicula.save()
            return redirect("listado")

    else:
        formulario = CrearPelicula(initial={
            "genero": pelicula.genero,
        })

    return render(request, "Inicio/actualizar_pelicula.html", {"formulario": formulario})


def eliminar_pelicula(request, id):
    pelicula = get_object_or_404(Pelicula, id=id)
    pelicula.delete()
    return redirect('listado')


def crear_pelicula(request):
    if request.method == 'POST':
        formulario = CrearPelicula(request.POST)

        if formulario.is_valid():
            info = formulario.cleaned_data

            pelicula = Pelicula(
                pelicula=info.get('pelicula'),
                genero=info.get('genero'),
                anio=info.get('anio'),
            )
            pelicula.save()

            return redirect('listado')

    else:
        formulario = CrearPelicula()

    return render(request, 'Inicio/crear_pelicula.html', {'formulario': formulario})


def listar_peliculas(request):

    formulario = BusquedaPeliculaForm(request.GET or None)

    if formulario.is_valid():
        pelicula= formulario.cleaned_data.get("pelicula")
        if pelicula:
            peliculas = Pelicula.objects.filter(pelicula__icontains=pelicula)
        else:
            peliculas = Pelicula.objects.all()
    else:
        peliculas = Pelicula.objects.all()

    return render(
        request,
        "Inicio/listar_peliculas.html",
        {
            "formulario": formulario,   "listado_de_peliculas": peliculas}
    )



def nueva(request):
    return render(request, "Inicio/nueva.html")



def inicio(request):
    return render(request, "Inicio/inicio.html")

from django.shortcuts import render, get_object_or_404
from .models import Pelicula

def ver_pelicula(request, id):
    pelicula = get_object_or_404(Pelicula, id=id)
    return render(request, 'Inicio/ver_pelicula.html', {'pelicula': pelicula})


