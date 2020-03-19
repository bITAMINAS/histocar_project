from webapp import views

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include

urlpatterns = [
    path("", views.index, name="index"),
    path('ver-servicios', views.verServicios, name='VerServicios'),
    path('crear-servicio', views.crearServicio, name='CrearServicio'),
    path('detalles-servicio/<int:servicio_id>', views.detallesServicio, name='DetallesServicio'),
    path('modificar-servicio/<int:pk>', views.editarServicio, name='ModificarServicio'),
    path('registro-usuario', views.crearUsuario, name='CrearUsuario'),
    path('crear-vehiculo', views.crearVehiculo, name='CrearVehiculo'),
    path('login', views.login, name='signin'),#el name se cambia de login a signin para que no de error en las vistas de recuperar password.
    path('logout', views.logout, name='logout'),
    path('listar-usuarios', views.verUsuarios, name='ListarUsuarios'),
    path('usuario-baja/<int:usuario_id>', views.bajaUsuario, name='UsuarioBaja'),
    path('registration/', include('django.contrib.auth.urls')),
    path('detalles-usuario/<int:usuario_id>', views.detallesUsuario, name='DetallesUsuario'),
]
