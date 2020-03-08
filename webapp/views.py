from django.shortcuts import render
from django.http import HttpResponse

#Cargamos vistas de los modelos
from .models import Servicio


# Create your views here.

#def index(request):
#    return HttpResponse("Hello, Djangoooooooooo! prueba de commit y si funciona servidor")

def test(request):
    return HttpResponse("Esta es una prueba de la pagina test")

def index(request):
    servicios = Servicio.objects.all().order_by('id')
    seccion = 'Inicio'
    return render(request, 'webapp/index.html', {'servicios': servicios, 'seccion': seccion})

def verServicios(request):
    servicios = Servicio.objects.all().order_by('id')
    seccion = 'Ver Servicios'
    return render(request, 'webapp/ver_servicios.html', {'servicios': servicios, 'seccion': seccion})

def crearServicio(request):
    servicios = Servicio.objects.all().order_by('id')
    seccion = 'Ver Servicios'
    return render(request, 'webapp/crear_servicio.html', {'servicios': servicios, 'seccion': seccion})
