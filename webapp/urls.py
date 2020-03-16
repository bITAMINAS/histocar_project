from django.urls import path
from webapp import views

urlpatterns = [
    path("", views.index, name="index"),
    path('ver-servicios', views.verServicios, name='VerServicios'),
    path('crear-servicio', views.crearServicio, name='CrearServicio'),
    path('detalles-servicio/<int:servicio_id>', views.detallesServicio, name='DetallesServicio'),
    path('registro-usuario', views.crearUsuario, name='CrearUsuario'),
    path('crear-vehiculo', views.crearVehiculo, name='CrearVehiculo'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('listar-usuarios', views.verUsuarios, name='ListarUsuarios')
]