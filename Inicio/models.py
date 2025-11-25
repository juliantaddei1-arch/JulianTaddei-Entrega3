from django.db import models

class Pelicula(models.Model):
    pelicula = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)
    anio = models.IntegerField()

   
    def __str__(self):
        return f'Pelicula({self.id}): {self.pelicula} - {self.genero} - {self.anio}'    