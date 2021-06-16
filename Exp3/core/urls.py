from django.urls import path
from .views import Inicio, Galeria

urlpatterns =[

    path ('', Inicio, name="Inicio"),
    path ('Galeria', Galeria, name="Galeria")
    
]