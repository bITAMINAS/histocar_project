from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#Cargamos los modelos
from .models import Servicio, Usuario, Vehiculo, EstadoServicio, Vehiculo
from .forms import ServicioForm, registroUsuario, Login, crearVehiculos, editarUsuarioForm 



def index(request):
    template_name='webapp/index.html'
    servicios = Servicio.objects.all().order_by('id')
    seccion = 'Inicio'
    return render(request, template_name, {'servicios': servicios, 'seccion': seccion})



# ---- vistas SERVICIO --------------------------------------------------------- 

@login_required(login_url='login')
def verServicios(request):
    template_name='webapp/servicios-lista.html'
    servicios = Servicio.objects.all().order_by('id')
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


def editarServicio(request, pk):
    seccion = 'Editar Servicio'
    servicio = Servicio.objects.get(pk=pk)
    estadoservicio = EstadoServicio.objects.get(servicio_id=pk)
    if request.method == "POST":
        form.fecha     = request.POST["fecha"]
        form.tareas    = request.POST["tareas"]
        form.textoOtros= request.POST["textoOtros"]
        form.kilometros= request.POST["kilometros"]
        form.costo     = request.POST["costo"]
        
        form.save()
        # estado = request.POST["estado"]
        
        #servicio1 = form.save(commit=False)
        #  if .estados.latest('estadoservicio__fecha') != servicio1.estado
        #      servicio.estados.add(estado)
             
           # servicio1.save()
            #form.save_m2m()
            
        #form = editarServicioForm(request.POST,instance=servicio)
        #if form.is_valid():
        #    estado = request.POST["estados"]
        #    servicio1 = form.save(commit=False)
        #    if servicio.estados.all() != estado:
        #        
        #        
        #    servicio1.save(force_insert=True)
        #    return redirect("VerServicios")
    else:
        form = editarServicioForm(instance = servicio)
    
    
    return render(request, 'webapp/servicios-modificar.html', {'servicio': servicio,'form': form, 'seccion': seccion})


# ---- vistas USUARIO ---------------------------------------------------------

def crearUsuario(request):
    template_name='webapp/crear_usuario.html'
    seccion = 'Alta de nuevo Usuario'
    if request.method == 'POST':
        form = registroUsuario(request.POST)
        if form.is_valid():
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
    seccion = 'Detalles de Usuario'
    return render(request, 'webapp/usuario-detalle.html', {'usuario': usuario, 'seccion': seccion})

def editarUsuario(request, pk):
    seccion = 'Editar Usuario'
    usuario = Usuario.objects.get(pk=pk)

    if request.method == "POST":
        form.name = request.POST['nombre']
        form.apellido = request.POST['apellido']
        form.email     = request.POST["email"]
        form.telefono    = request.POST["telefono"]
        
        form.save()
    
    else:
        form = editarUsuarioForm(instance = usuario)
    
    
    return render(request, 'webapp/usario-editar.html', {'usuario': usuario,'form': form, 'seccion': seccion})  

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