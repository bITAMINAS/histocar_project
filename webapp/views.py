from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone

#Cargamos vistas de los modelos
from .models import Servicio
from .forms import ServicioForm

# Create your views here.

def index(request):
    servicios = Servicio.objects.all().order_by('id')
    seccion = 'Inicio'
    return render(request, 'webapp/index.html', {'servicios': servicios, 'seccion': seccion})

def verServicios(request):
    servicios = Servicio.objects.all().order_by('id')
    seccion = 'Ver Servicios'
    return render(request, 'webapp/servicios-lista.html', {'servicios': servicios, 'seccion': seccion})

def crearServicio(request):
    seccion = 'Crear Servicio'

    if request.method == "POST":
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form= ServicioForm()
    return render(request, 'webapp/servicios-crear.html', {'form': form, 'seccion': seccion})

def detallesServicio(request, servicio_id):
    servicio = Servicio.objects.get(pk=servicio_id)
    seccion = 'Detalles de Servicio'
    return render(request, 'webapp/servicios-detalle.html', {'servicio': servicio, 'seccion': seccion})