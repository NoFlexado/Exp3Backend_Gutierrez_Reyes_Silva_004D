from django.shortcuts import render, redirect, get_object_or_404
from .models import Donacion
from .forms import ObjetoForm

# Create your views here.
def Inicio(request):
    return render(request,'Inicio.html')

def Galeria(request):
    donaciones = Donacion.objects.all()
    return render(request,'Galeria.html', context={'donaciones': donaciones},)

def Formulario(request):
    return render(request,'Formulario2.html')

def Lista(request):
    donaciones = Donacion.objects.all()
    return render(request,'Lista.html', context={'donaciones': donaciones},)


def form_objeto(request):
    if request.method == "POST":
        objeto_form = ObjetoForm(request.POST,request.FILES)
        if objeto_form.is_valid():
            post = objeto_form.save(commit=False)
            post.save()
            return redirect('Lista')
    else:
        objeto_form = ObjetoForm()
        return render(request, 'core/form_crear.html', {'objeto_form': objeto_form})

def mod_objeto(request, pk):
    post = get_object_or_404(Donacion, pk=pk)
    if request.method == "POST":
        objeto_form = ObjetoForm(request.POST, request.FILES, instance=post)
        if objeto_form.is_valid():
            post = objeto_form.save()
            post.save()
            return redirect('Lista')
    else:
        objeto_form = ObjetoForm(instance=post)
    return render(request, 'core/mod_objeto.html', {'objeto_form': objeto_form})

def delete_objeto(request, pk):
    objeto = Donacion.objects.get(pk=pk)
    objeto.delete()
    return redirect('Lista')