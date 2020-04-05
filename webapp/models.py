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
    
    Departamentos = models.TextChoices('Departamentos', 'Artigas Canelones Cerro_Largo Colonia Durazno Flores Florida Lavalleja Maldonado Montevideo Paysandú Río_Negro Rivera Rocha Salto San_José Soriano Tacuarembó Treinta_y_Tres')
    
    nombre = models.CharField(max_length=20, default="")
    apellido = models.CharField(max_length=20, default="")
    documento = models.CharField(unique=True, max_length=8, default="")
    email = models.EmailField(unique=True, default="") #unique=True sirve para que no se repita en la bd
    telefono = models.CharField('Teléfono', max_length=20, default="")
    tipoUsuario = models.IntegerField('Tipo de usuario', default=1) # 1=CLiente, 2=Empleado, 3=Administrador
    dirDepartamento = models.CharField('Departamento', choices=Departamentos.choices, max_length=20, default="")
    dirCiudad = models.CharField('Ciudad', max_length=20, default="")
    dirCalle = models.CharField('Calle', max_length=50, default="")
    dirNumero = models.CharField('Número', max_length=5, default="")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_client = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'documento'
    REQUIRED_FIELDS = ['email','telefono']
    objects = UsuarioMejorado()
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido


#=== MANAGERS ========================================

# class ServicioManager(models.Manager):
    



# class EstadoManager(models.Manager):
#     def get_latest_estado_obj(self, estado):
#         return self.get_queryset().filter(nombre=estado).latest()


class Servicio(models.Model):
    fecha = models.DateTimeField()
    textoOtros = models.TextField('Otras tareas', max_length=240, default="")
    comentario = models.CharField(max_length=240, default="")
    kilometros = models.IntegerField('Kilómetros', default=0)
    puntuacion = models.IntegerField('Calificación',default=0)
    costo = models.IntegerField(default=0)
    vehiculo = models.ForeignKey('Vehiculo', on_delete=models.CASCADE, default="", verbose_name='Vehículo')
    tareas = models.ManyToManyField('Tarea')
    estados = models.ManyToManyField('Estado', through='EstadoServicio', verbose_name='Estado')
    estadoAc = models.IntegerField(default=0)

    @property
    def estadoActual(self):
        estado = self.estados.latest('estadoservicio__fecha')
        return estado.nombre

    def __str__(self):
        return datetime.strftime(self.fecha, '%d/%m/%Y') + ', ' + self.vehiculo.modelo.marca.nombre + ' ' + self.vehiculo.modelo.nombre

    def get_absolute_url(self): # new
        return reverse('university_detail', args=[str(self.id)])

    # https://learndjango.com/tutorials/django-best-practices-models#


class Tarea(models.Model):
    nombre = models.CharField(max_length=240, default="")

    def __str__(self):
        return self.nombre


class Estado(models.Model):
    nombre = models.CharField(max_length=50, default="")
    descripcion = models.CharField('Descripción',max_length=240, default="")

    def __str__(self):
        return self.nombre


# Relación N:N entre Estado<>Servicio
class EstadoServicio(models.Model):
    servicio = models.ForeignKey('Servicio', on_delete=models.CASCADE)
    estado = models.ForeignKey('Estado', on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=datetime.now())

    class Meta:
        get_latest_by = "fecha"

class Vehiculo(models.Model):
    TiposCombustibles = models.TextChoices('Combustible', 'Nafta Gasoil Híbrido Eléctrico Hidrógeno GLP')
    Colores = models.TextChoices('Color', 'Blanco Rojo Negro Azul Bordó Marrón Gris_Plata Gris_Ceniza Amarillo Verde Otro')
  
    modelo = models.ForeignKey('Modelo', on_delete=models.CASCADE) # Con el atributo modelo ya es suficiente, ya que a partir de él se puede inferir la Marca
    color = models.CharField(blank=True, choices=Colores.choices, max_length=15)
    nroChasis = models.CharField('Número de chasis', max_length=50, default="")
    matricula = models.CharField('Matrícula', max_length=50, default="")
    anio = models.IntegerField('Año',default=2020)
    tipoCombustible = models.CharField('Tipo de combustible', blank=True, choices=TiposCombustibles.choices, max_length=15)
    duenio = models.ForeignKey('Usuario', on_delete=models.CASCADE, verbose_name='Propietario')
   
    def __str__(self):
        return self.modelo.marca.nombre + ' ' + self.modelo.nombre + ' - ' + self.matricula + ' - ' + self.duenio.nombre + ' '+ self.duenio.apellido


class Marca(models.Model):
    nombre = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.nombre


class Modelo(models.Model):
    nombre = models.CharField(max_length=20, default="")
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE) #Modelo pertenece a una Marca

    def __str__(self):
        return self.marca.nombre + ' ' + self.nombre 