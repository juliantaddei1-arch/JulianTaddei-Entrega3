from django.urls import path
from Inicio.views import Inicio, nueva, crear_pelicula, listar_peliculas

urlpatterns = [

    path('', Inicio),
    path('nueva/', nueva),
    path('crear_pelicula/<pelicula>/<genero>/', crear_pelicula),
    path('listado_peliculas/', listar_peliculas)

]
