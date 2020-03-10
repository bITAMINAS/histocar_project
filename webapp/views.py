from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone

#Cargamos vistas de los modelos
from .models import Servicio
from .forms import ServicioForm

# Create your views here.

#def index(request):
#    return HttpResponse("Hello, Djangoooooooooo! prueba de commit y si funciona servidor")

#def test(request):
#    return HttpResponse("Esta es una prueba de la pagina test")

def index(request):
    servicios = Servicio.objects.all().order_by('id')
    seccion = 'Inicio'
    return render(request, 'webapp/index.html', {'servicios': servicios, 'seccion': seccion})

def verServicios(request):
    servicios = Servicio.objects.all().order_by('id')
    seccion = 'Ver Servicios'
    return render(request, 'webapp/ver_servicios.html', {'servicios': servicios, 'seccion': seccion})

def crearServicio(request):
    seccion = 'Crear Servicio'

    if request.method == "POST":
        form = ServicioForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form= ServicioForm()
    return render(request, 'webapp/crear_servicio.html', {'form': form, 'seccion': seccion})
