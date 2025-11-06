from django.urls import path
from Inicio.views import Inicio, nueva

urlpatterns = [

    path('', Inicio),
    path('nueva/', nueva),
]
