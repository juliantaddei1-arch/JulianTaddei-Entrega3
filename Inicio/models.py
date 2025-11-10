from django.db import models

class Pelicula(models.Model):
    pelicula = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)
   
    