from django.urls import path
from webapp import views

urlpatterns = [
    path("", views.index, name="index"),
    path('ver-servicios', views.verServicios, name='VerServicios'),
    path('crear-servicio', views.crearServicio, name='CrearServicio'),
    path('registro', views.altaUsuario, name='AltaUsuario'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]