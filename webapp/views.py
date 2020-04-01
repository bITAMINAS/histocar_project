from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from datetime import datetime
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#Cargamos los modelos
from .models import Servicio, Usuario, Vehiculo, EstadoServicio, Estado
from .forms import ServicioForm, registroUsuario, Login, crearVehiculos, editarServicioForm



def index(request):
    template_name='webapp/index.html'
    servicios = Servicio.objects.all().order_by('id')
    seccion = 'Inicio'
    return render(request, template_name, {'servicios': servicios, 'seccion': seccion})



# ---- vistas SERVICIO --------------------------------------------------------- 

@login_required(login_url='login')
def verServicios(request):
    template_name='webapp/servicios-lista.html'
    servicios = Servicio.objects.all() #.order_by('id')
    servicios
    seccion = 'Ver Servicios'
    return render(request, template_name, {'servicios': servicios, 'seccion': seccion})


@login_required(login_url='login')
def crearServicio(request):

    seccion = 'Crear Servicio'

    if request.method == "POST":
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se creo el servicio correctamente')
            return redirect('index')
            
    else:
        form= ServicioForm()
    return render(request, 'webapp/servicios-crear.html', {'form': form, 'seccion': seccion})


def detallesServicio(request, servicio_id):
    servicio = Servicio.objects.get(pk=servicio_id)
    seccion = 'Detalles de Servicio'
    return render(request, 'webapp/servicios-detalle.html', {'servicio': servicio, 'seccion': seccion})


def editarServicio(request, servicio_id):
    seccion = 'Editar Servicio'
    servicio = Servicio.objects.get(pk=servicio_id)
    estadoAnteriorServicio = servicio.estados.latest('estadoservicio__fecha').id

    if request.method == "POST":
        form = editarServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            FormEstado_id = request.POST["estados"]
            print('Estadooooooooooo:' + FormEstado_id)
            pending_servicio = form.save(commit=False)                    
            
            estadoActualServicio = int(FormEstado_id)
            
            #si el estado_id del form es distinto al al ultimo estado_id registrado
            if estadoAnteriorServicio != estadoActualServicio:               
                e=Estado.objects.get(pk=estadoActualServicio)
                s=servicio
                
                servicioEstado = EstadoServicio(estado=e, servicio=s, fecha=datetime.now())
                servicioEstado.save()
            return redirect("VerServicios")

    else:
        form = editarServicioForm(initial={'estados':estadoAnteriorServicio}, instance = servicio)
        
    return render(request, 'webapp/servicios-modificar.html', {'servicio': servicio,'form': form, 'seccion': seccion})


# ---- vistas USUARIO ---------------------------------------------------------

def crearUsuario(request):
    template_name='webapp/usuarios-crear.html'
    seccion = 'Alta de nuevo Usuario'
    if request.method == 'POST':
        form = registroUsuario(request.POST)
        if form.is_valid():
            permiso = request.POST["permiso"]
            print('permisooooooooooo:' + permiso)
            form.save()
            messages.success(request, 'Usuario creado correctamente')
            return redirect('index')
    else:
        form = registroUsuario()
    return render(request, template_name, {'form': form, 'seccion': seccion})


@login_required(login_url='login')
def verUsuarios(request):
    template_name='webapp/usuarios-lista.html'
    usuarios = Usuario.objects.all().order_by('id')
    seccion = 'Ver Usuarios'
    return render(request, template_name, {'usuarios': usuarios, 'seccion': seccion})

def detallesUsuario(request, usuario_id):
    usuario = Usuario.objects.get(pk=usuario_id)
    vehiculos = Vehiculo.objects.filter(duenio__id=usuario_id)
    servicios = Servicio.objects.filter(vehiculo__duenio__id=usuario_id)
    seccion = 'Detalles de Usuario'
    return render(request, 'webapp/usuario-detalle.html', {'usuario': usuario, 'seccion': seccion, 'vehiculos': vehiculos, 'servicios': servicios})

def bajaUsuario(request, usuario_id):
    # Recuperamos la instancia de la persona
    instancia = Usuario.objects.get(id=usuario_id)
    instancia.is_active=False
    instancia.save()
    messages.success(request, 'Usuario dado de baja existosamente.')
    # Después redireccionamos de nuevo a la lista
    return redirect('ListarUsuarios')



# ---- vistas VEHÍCULO ---------------------------------------------------------

def crearVehiculo(request):
    template_name='webapp/vehiculo-crear.html'
    seccion = 'Alta de nuevo vehiculo'
    if request.method == 'POST':
        form = crearVehiculos(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehiculo creado y asignado correctamente')
            return redirect('index')
    else:
        form = crearVehiculos()
    return render(request, template_name, {'form': form, 'seccion': seccion})



# ---- vistas LOGIN ---------------------------------------------------------

def login(request):
    seccion= 'Ingreso de usuario'
    if request.method == 'POST':
        form = Login(data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    return redirect('/') 
    else:
        form = Login()

    return render(request,'registration/login.html',{'form':form, 'seccion': seccion})


def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')
###############################################################################
###############################################################################
###############################################################################
####VISTAS CLIENTE###############

####Vista listar vehiculos#####
@login_required(login_url='login')
def verVehiculosCliente(request):
    template_name='webapp/cliente/vehiculo-listar.html'
    usuario = request.user.id
    vehiculos = Vehiculo.objects.all().filter(duenio_id=usuario)
    seccion = 'Ver mis vehiculos'
    return render(request, template_name, {'vehiculos': vehiculos, 'seccion': seccion})

@login_required(login_url='login')
def borrarVehiculoCliente(request, vehiculo_id):
    usuario = request.user.id
    #obtengo el id del vehiculo a borrar
    instancia = Vehiculo.objects.get(id=vehiculo_id)
    #reviso que el vehiculo pertenezca al usuario logueado actualmente
    if usuario == instancia.duenio_id:
        instancia.delete()
        messages.success(request, 'Vehiculo dado de baja correctamente')    
    else:
        messages.warning(request, 'Ocurrio un problema, quizas no es tu vehiculo.')

    return redirect('VerVehiculos')