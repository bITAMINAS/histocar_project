from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth import authenticate, login as django_login, logout as django_logout

#Cargamos vistas de los modelos
from .models import Servicio, Usuario
from .forms import ServicioForm, registroUsuario, Login

# Create your views here.

def index(request):
    template_name='webapp/index.html'
    servicios = Servicio.objects.all().order_by('id')
    seccion = 'Inicio'
    return render(request, template_name, {'servicios': servicios, 'seccion': seccion})


def verServicios(request):
    template_name='webapp/servicios-lista.html'
    seccion = 'Ver Servicios'
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

def crearUsuario(request):
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

def login(request):
    seccion= 'Ingreso de usuario'
    template_name='webapp/login.html'
    if request.method == 'POST':
        form = Login(data = request.POST)
        if form.is_valid():
            documento = request.POST['documento']
            password = request.POST['password']
            user = authenticate(documento=documento, password=password)
            if user is not None:
                if user.is_active:
                    django_login(request,user)
                    return redirect('/') 
    else:
        form = Login()

    return render(request, template_name, {'form':form, 'seccion': seccion})

def logout(request):
    django_logout(request)
    return redirect('/')