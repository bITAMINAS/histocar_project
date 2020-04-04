from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from datetime import datetime
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#Cargamos los modelos
from .models import Servicio, Usuario, Vehiculo, EstadoServicio, Estado
from .forms import ServicioForm, registroUsuario, Login, crearVehiculos, editarServicioForm, editarUsuarioForm



@login_required(login_url='login')
def index(request):
    template_name='webapp/index.html'
    servicios = Servicio.objects.all().order_by('id')
    ssIngresados = servicios.filter(estadoAc=11)
    ssEnProgreso = servicios.filter(estadoAc=12)
    ssSuspendido = servicios.filter(estadoAc=13)
    ssFinalizado = servicios.filter(estadoAc=14)
    ssParaRetirar = servicios.filter(estadoAc=15)
    ssRetirado = servicios.filter(estadoAc=16)
    print(ssIngresados)
    #print(ssIngresados)
    seccion = 'Inicio'
    context = {'servicios': servicios, 'seccion': seccion, 'ssIngresados': ssIngresados, 'ssEnProgreso': ssEnProgreso,
                'ssSuspendido': ssSuspendido, 'ssFinalizado': ssFinalizado, 'ssParaRetirar': ssParaRetirar, 'ssRetirado': ssRetirado}
    return render(request, template_name, context)




# ---- vistas SERVICIO --------------------------------------------------------- 

@login_required(login_url='login')
def serviciosView(request):
    template_name='webapp/servicios-lista.html'
    servicios = Servicio.objects.all() #.order_by('id')
    
    seccion = 'Servicios'
    return render(request, template_name, {'servicios': servicios, 'seccion': seccion})


@login_required(login_url='login')
def crearServicio(request):
    seccion = 'Servicios'

    if request.method == "POST":
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se creo el servicio correctamente')
            return redirect('index')
            
    else:
        form= ServicioForm()
    return render(request, 'webapp/servicios-crear.html', {'form': form, 'seccion': seccion})


def servicioView(request, servicio_id):
    servicio = Servicio.objects.get(pk=servicio_id)
    seccion = 'Detalles de Servicio'
    return render(request, 'webapp/servicios-detalle.html', {'servicio': servicio, 'seccion': seccion})

def editarServicio(request, servicio_id):
    seccion = 'Servicios'
    servicio = Servicio.objects.get(pk=servicio_id)
    estadoAnteriorServicio = servicio.estados.latest('estadoservicio__fecha').id

    if request.method == "POST":
        form = editarServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            FormEstado_id = request.POST["estados"]

            pending_servicio = form.save(commit=False)                    
            
            estadoActualServicio = int(FormEstado_id)
            pending_servicio.estadoAc = estadoActualServicio

            #si el estado_id del form es distinto al al ultimo estado_id registrado
            if estadoAnteriorServicio != estadoActualServicio:               
                e=Estado.objects.get(pk=estadoActualServicio)
                s=pending_servicio
                
                servicioEstado = EstadoServicio(estado=e, servicio=s, fecha=datetime.now())
                
                servicioEstado.save()
            #servicio.save()
            pending_servicio.save()
            return redirect("Servicios")

    else:
        form = editarServicioForm(initial={'estados':estadoAnteriorServicio}, instance = servicio)
        
    return render(request, 'webapp/servicios-modificar.html', {'servicio': servicio,'form': form, 'seccion': seccion})



def borrarServicio(request, servicio_id):
    instancia = Servicio.objects.get(id=servicio_id)
    instancia.delete()
    messages.success(request, 'Servicio dado de baja existosamente.')
    return redirect('Servicios')


# ---- vistas USUARIO ---------------------------------------------------------

def crearUsuario(request):
    template_name='webapp/usuarios-crear.html'
    seccion = 'Usuarios'
    if request.method == 'POST':
        form = registroUsuario(request.POST)
        if form.is_valid():
            tipo_de_usuario = int(request.POST["tipo_de_usuario"])
            
            pending_usuario = form.save(commit=False)
            if tipo_de_usuario == 1 :
                pending_usuario.is_client = True
            else:
                pending_usuario.is_client = False
                pending_usuario.is_staff = True
            pending_usuario.save()

            messages.success(request, 'Usuario creado correctamente')
            return redirect('index')
    else:
        form = registroUsuario()
    return render(request, template_name, {'form': form, 'seccion': seccion})


@login_required(login_url='login')
def verUsuarios(request):
    template_name='webapp/usuarios-lista.html'
    usuarios = Usuario.objects.filter(is_client=False, is_active=True).order_by('id')
    seccion = 'Usuarios'
    return render(request, template_name, {'usuarios': usuarios, 'seccion': seccion})

def detallesUsuario(request, usuario_id):
    usuario = Usuario.objects.get(pk=usuario_id)
    vehiculos = Vehiculo.objects.filter(duenio__id=usuario_id)
    servicios = Servicio.objects.filter(vehiculo__duenio__id=usuario_id)
    seccion = 'Detalles de Usuario'
    return render(request, 'webapp/usuario-detalle.html', {'usuario': usuario, 'seccion': seccion, 'vehiculos': vehiculos, 'servicios': servicios})
  

def editarUsuario(request, pk):
    seccion = 'Usuarios'
    usuario = Usuario.objects.get(pk=pk)
    form = editarUsuarioForm(request.POST, instance = usuario)
    if request.method == "POST":
        if form.is_valid():
            usuario=form.save()
            usuario.save()
            messages.success(request, 'Usuario editado exitosamente.')
            return redirect('ListarUsuarios')
    else:
        form = editarUsuarioForm(instance=usuario)
    
    return render(request, 'webapp/usuario-editar.html', {'usuario': usuario, 'seccion': seccion, 'form': form})  


def editarUsuario(request, pk):
    seccion = 'Editar Usuario'
    usuario = Usuario.objects.get(pk=pk)
    form = editarUsuarioForm(request.POST, instance = usuario)
    if request.method == "POST":
        if form.is_valid():
            usuario=form.save()
            usuario.save()
            messages.success(request, 'Usuario editado exitosamente.')
            return redirect('ListarUsuarios')
    else:
        form = editarUsuarioForm(instance=usuario)
    
    
    return render(request, 'webapp/usuario-editar.html', {'usuario': usuario, 'seccion': seccion, 'form': form})  

def bajaUsuario(request, usuario_id):
    # Recuperamos la instancia de la persona
    instancia = Usuario.objects.get(id=usuario_id)
    instancia.is_active=False
    instancia.save()
    messages.success(request, 'Usuario dado de baja existosamente.')

    redirecto_to = 'ListarUsuarios'
    if instancia.is_client:
        redirecto_to = 'Clientes'

    # Después redireccionamos...
    return redirect(redirecto_to)




# ---- vistas CLIENTES ---------------------------------------------------------

@login_required(login_url='login')
def clienteView(request, usuario_id):
    usuario = Usuario.objects.get(pk=usuario_id)
    vehiculos = Vehiculo.objects.filter(duenio__id=usuario_id)
    servicios = Servicio.objects.filter(vehiculo__duenio__id=usuario_id)
    seccion = 'Detalles de cliente'
    return render(request, 'webapp/usuario-detalle.html', {'usuario': usuario, 'seccion': seccion, 'vehiculos': vehiculos, 'servicios': servicios})



@login_required(login_url='login')
def clientesView(request):
    template_name='webapp/clientes-lista.html'
    usuarios = Usuario.objects.filter(is_client=True, is_active=True).order_by('id')
    seccion = 'Clientes'
    return render(request, template_name, {'usuarios': usuarios, 'seccion': seccion})


@login_required(login_url='login')
def clienteCrearView(request):
    template_name='webapp/clientes-crear.html'
    usuarios = Usuario.objects.all().order_by('id')
    seccion = 'Nuevo cliente'
    return render(request, template_name, {'usuarios': usuarios, 'seccion': seccion})



# ---- vistas VEHÍCULO ---------------------------------------------------------

def crearVehiculo(request):
    template_name='webapp/vehiculo-crear.html'
    seccion = 'Vehículo'
    if request.method == 'POST':
        form = crearVehiculos(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehiculo creado y asignado correctamente')
            return redirect('index')
    else:
        form = crearVehiculos()
    return render(request, template_name, {'form': form, 'seccion': seccion})

def crearVehiculoCliente(request, duenio_id):
    template_name='webapp/cliente/vehiculo-crear-cliente.html'
    seccion = 'Vehículo'
    if request.method == 'POST':
        form = crearVehiculosCliente(request.POST)
        if form.is_valid():
            cliente = Vehiculo(duenio_id = usuario)
            cliente.save()
            form.save()
            messages.success(request, 'Vehiculo creado y asignado correctamente')
            return redirect('index')
    else:
        form = crearVehiculosCliente()
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
