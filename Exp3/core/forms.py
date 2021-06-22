from django import forms
from .models import Donacion, Categoria
from django.forms import ModelForm,widgets




class ObjetoForm(forms.ModelForm):


    
    nombreObjeto = forms.CharField(label='NombreArtículo',max_length=200, widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'name': 'Artículo',
            'placeholder': 'Ingrese el nombre del artículo'
        }
    ))
    
    descripcion = forms.CharField(label='Descripción', max_length=1000, widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'name': 'Descripcion',
            'placeholder': 'Escriba una descripción de su artículo'
        }
    ))
    
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), label='Categoría',
            widget=forms.Select(
            attrs={
                'class':'form-control' 
            }
            ))
    image = forms.ImageField(label='Imagen',
            widget=forms.ClearableFileInput(
            attrs={
                'class':'form-control' 
            }
            ))
    

    class Meta:
        model = Donacion
        fields = ('nombreObjeto','descripcion', 'categoria', 'image',)