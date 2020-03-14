from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import UsuarioMejorado
from datetime import datetime
from django.utils import timezone


class Usuario(AbstractBaseUser, PermissionsMixin):
    #basado en la documentacion de django
    #https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#extending-the-existing-user-model
    nombre = models.CharField(max_length=20, default="")
    apellido = models.CharField(max_length=20, default="")
    documento = models.CharField(unique=True, max_length=8, default="")
    email = models.EmailField(unique=True, default="") #unique=True sirve para que no se repita en la bd
    telefono = models.CharField(max_length=20, default="")
    tipoUsuario = models.IntegerField(default=0)
    dirDepartamento = models.CharField('Departamento',max_length=20, default="")
    dirCiudad = models.CharField(max_length=20, default="")
    dirCalle = models.CharField(max_length=50, default="")
    dirNumero = models.CharField(max_length=5, default="")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'documento'
    REQUIRED_FIELDS = ['email','telefono']
    objects = UsuarioMejorado()
    def __str__(self):
        return self.documento
    
class Servicio(models.Model):
    fecha = models.DateTimeField(default="10/10/2020 22:22:00")
    textoOtros = models.CharField(max_length=240, default="")
    comentario = models.CharField(max_length=240, default="")
    kilometros = models.IntegerField(default=0)
    puntuacion = models.IntegerField(default=0)
    costo = models.IntegerField(default=0)
    vehiculo = models.ForeignKey('Vehiculo', on_delete=models.CASCADE, default="")
    tareas = models.ManyToManyField('Tarea')
    estados = models.ManyToManyField('Estado', through='EstadoServicio')

    def __str__(self):
        return datetime.strftime(self.fecha, '%d/%m/%Y') + ', ' + self.vehiculo.modelo.marca.nombre + ' ' + self.vehiculo.modelo.nombre

class Tarea(models.Model):
    nombre = models.CharField(max_length=240, default="")

    def __str__(self):
        return self.nombre

class Estado(models.Model):
    nombre = models.CharField(max_length=50, default="")
    descripcion = models.CharField(max_length=240, default="")

    def __str__(self):
        return self.nombre

# Relación N:N entre Estado<>Servicio
class EstadoServicio(models.Model):
    servicio = models.ForeignKey('Servicio', on_delete=models.CASCADE)
    estado = models.ForeignKey('Estado', on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=datetime.now())
    # fecha queda como campo null = true porque es el fix del bug 7
    # https://exceptionshub.com/not-null-constraint-failed-after-adding-to-models-py.html


class Vehiculo(models.Model):
    TiposCombustibles = models.TextChoices('Combustible', 'Nafta Gasoil Híbrido Eléctrico Hidrógeno GLP')
    Colores = models.TextChoices('Color', 'Blanco Rojo Negro Azul Bordó Marrón Gris_Plata Gris_Ceniza Amarillo Verde Otro')
  
    modelo = models.ForeignKey('Modelo', on_delete=models.CASCADE) # Con el atributo modelo ya es suficiente, ya que a partir de él se puede inferir la Marca
    color = models.CharField(blank=True, choices=Colores.choices, max_length=15)
    nroChasis = models.CharField(max_length=50, default="")
    matricula = models.CharField(max_length=50, default="")
    anio = models.IntegerField(default=0)
    tipoCombustible = models.CharField(blank=True, choices=TiposCombustibles.choices, max_length=15)
    duenio = models.ForeignKey('Usuario', on_delete=models.CASCADE)
   
    def __str__(self):
        return self.modelo.marca.nombre + ' ' + self.modelo.nombre + ' - ' + self.matricula

class Marca(models.Model):
    nombre = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.nombre

class Modelo(models.Model):
    nombre = models.CharField(max_length=20, default="")
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE) #Modelo pertenece a una Marca

    def __str__(self):
        return self.nombre