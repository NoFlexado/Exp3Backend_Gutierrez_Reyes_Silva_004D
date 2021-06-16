from django.urls import path
from .views import Inicio, Galeria, Formulario

urlpatterns =[

    path ('', Inicio, name="Inicio"),
    path ('Galeria', Galeria, name="Galeria"),
    path ('Formulario', Formulario, name="Formulario")
    
]