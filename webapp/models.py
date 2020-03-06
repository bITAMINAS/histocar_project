from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    documento = models.CharField(max_length=8)
    email = models.EmailField(unique=True, default="") #unique=True sirve para que no se repita en la bd
    telefono = models.CharField(max_length=20)
    tipoUsuario = models.IntegerField(default=0)
    dirDepartamento = models.CharField(max_length=20)
    dirCiudad = models.CharField(max_length=20)
    dirCalle = models.CharField(max_length=50)
    dirNumero = models.CharField(max_length=5)
    
class Servicio(models.Model):
    fecha = models.DateTimeField()
    textoOtros = models.CharField(max_length=240)
    comentario = models.CharField(max_length=240)
    kilometros = models.IntegerField 
    puntuacion = models.IntegerField 
    costo = models.IntegerField 
    
class Tarea(models.Model):
    nombre = models.CharField(max_length=240)
    
class Estado(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=240)
    servicio = models.ManyToManyField(Servicio)
    fecha = models.DateTimeField()

class Vehiculo(models.Model):
    modelo = models.ForeignKey(Modelo)
    color = models.CharField(max_length=10)
    nroChasis = models.CharField(max_length=50)
    matricula = models.CharField(max_length=50)
    anio = models.IntegerField 
    tipoCombustible =

class Marca(models.Model):
    nombre = models.CharField(max_length=20)

class Modelo(models.Model):
    nombre = models.CharField(max_length=20)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE) #Modelo pertenece a una Marca

class TipoCombustible(models.Model):
    nombre = models.CharField(max_length=20)

