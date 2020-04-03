from webapp import views

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include

urlpatterns = [
    path("", views.index, name="index"),
    path('servicios', views.serviciosView, name='Servicios'),
    path('crear-servicio', views.crearServicio, name='CrearServicio'),
    path('servicio/<int:servicio_id>', views.servicioView, name='Servicio'),
    path('modificar-servicio/<int:servicio_id>', views.editarServicio, name='ModificarServicio'),
    path('eliminar-servicio/<int:servicio_id>', views.borrarServicio, name='BorrarServicio'),
    path('registro-usuario', views.crearUsuario, name='CrearUsuario'),
    path('crear-vehiculo', views.crearVehiculo, name='CrearVehiculo'),
    path('login', views.login, name='signin'),#el name se cambia de login a signin para que no de error en las vistas de recuperar password.
    path('logout', views.logout, name='logout'),
    path('listar-usuarios', views.verUsuarios, name='ListarUsuarios'),
    path('usuario-baja/<int:usuario_id>', views.bajaUsuario, name='UsuarioBaja'),
    path('registration/', include('django.contrib.auth.urls')),
    path('detalles-usuario/<int:usuario_id>', views.detallesUsuario, name='DetallesUsuario'),
    path('ver-vehiculos', views.verVehiculosCliente, name='VerVehiculos'),
    path('vehiculo-baja/<int:vehiculo_id>', views.borrarVehiculoCliente, name="BorrarVehiculoCliente"),
    # Clientes
    path('clientes', views.clientesView, name='Clientes'),
    path('cliente', views.clienteView, name='Cliente'),
    path('cliente-crear', views.clienteCrearView, name='ClienteCrear'),

    path('perfil-vehiculo-alta', views.crearVehiculoCliente, name='AltaVehiculoCliente'),
    path('editar-usuario/<int:pk>', views.editarUsuario, name='EditarUsuario'),
]
