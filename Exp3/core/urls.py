from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from .views import Inicio, Galeria, Formulario, Lista, form_objeto, mod_objeto

urlpatterns =[

    path ('', Inicio, name="Inicio"),
    path ('Galeria', Galeria, name="Galeria"),
    path ('Formulario', Formulario, name="Formulario"),
    path ('Lista', Lista , name="Lista"),
    path ('form_objeto', form_objeto, name='form_objeto'),
    path ('mod_objeto/<str:pk>', mod_objeto, name="mod_objeto" )
]



if settings.DEBUG:urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)