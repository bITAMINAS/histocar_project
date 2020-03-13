from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth import authenticate, login

#Cargamos vistas de los modelos
from .models import Servicio, Usuario
from .forms import ServicioForm, registroUsuario

# Create your views here.

def index(request):
    template_name='webapp/index.html'
    servicios = Servicio.objects.all().order_by('id')
    seccion = 'Inicio'
    return render(request, template_name, {'servicios': servicios, 'seccion': seccion})

def verServicios(request):
    template_name='webapp/servicios-lista.html'
    seccion = 'Ver Servicios'
    servicios = Servicio.objects.all().order_by('id')
    
    return render(request, template_name, {'servicios': servicios, 'seccion': seccion})

def crearServicio(request):
    template_name='webapp/servicios-crear.html'
    seccion = 'Crear Servicio'

    if request.method == "POST":
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form= ServicioForm()
    return render(request, template_name, {'form': form, 'seccion': seccion})

def detallesServicio(request, servicio_id):
    template_name='webapp/servicios-detalle.html'
    seccion = 'Detalles de Servicio'
    
    servicio = Servicio.objects.get(pk=servicio_id)
    return render(request, template_name, {'servicio': servicio, 'seccion': seccion})

def altaUsuario(request):
    template_name='webapp/registro.html'
    seccion = 'Alta de nuevo Usuario'
    
    if request.method == 'POST':
        form = registroUsuario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = registroUsuario()
    return render(request, template_name, {'form': form})
