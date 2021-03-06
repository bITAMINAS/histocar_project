from webapp import views
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include

urlpatterns = [
    path("", views.index, name="index"),
    # Servicios
    path('servicios', views.serviciosView, name='Servicios'),
    path('crear-servicio', views.crearServicio, name='CrearServicio'),
    path('servicio/<int:servicio_id>', views.servicioView, name='Servicio'),
    path('modificar-servicio/<int:servicio_id>', views.editarServicio, name='ModificarServicio'),
    path('servicio-borrar/<int:servicio_id>', views.borrarServicio, name='BorrarServicio'),
    # Usuarios
    path('login', views.login, name='signin'),#el name se cambia de login a signin para que no de error en las vistas de recuperar password.
    path('logout', views.logout, name='logout'),
    path('registro-usuario', views.crearUsuario, name='CrearUsuario'),
    path('listar-usuarios', views.verUsuarios, name='ListarUsuarios'),
    path('usuario-baja/<int:usuario_id>', views.bajaUsuario, name='UsuarioBaja'),
    path('registration/', include('django.contrib.auth.urls')),
    path('detalles-usuario/<int:usuario_id>', views.detallesUsuario, name='DetallesUsuario'),
    path('editar-usuario/<int:pk>', views.editarUsuario, name='EditarUsuario'),
    # Vehículos
    path('ver-vehiculos', views.verVehiculosCliente, name='VerVehiculos'),
    path('crear-vehiculo', views.crearVehiculo, name='CrearVehiculo'),
    path('vehiculo-baja/<int:vehiculo_id>', views.borrarVehiculoCliente, name="BorrarVehiculoCliente"),
    path('crear-vehiculo-cliente', views.crearVehiculoCliente, name='crearVehiculoCliente'),
    # Clientes
    path('clientes', views.clientesView, name='Clientes'),
    path('cliente/<int:usuario_id>', views.clienteView, name='Cliente'),
    path('cliente-crear', views.clienteCrearView, name='ClienteCrear'),

    
    
   
]
