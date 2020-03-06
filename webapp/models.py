from django.db import models

# Create your models here.

class Usuario(models.Model):
    """Se crea el modelo usuario"""
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    documento = models.CharField(max_length=8)
    email = models.EmailField(unique=True, default="") #unique=True sirve para que no se repita en la bd
    telefono = models.CharField(max_length=20)
    tipoUsuario = models.IntegerField(default=0)
    direccion = models.CharField(max_length=200)
    
class Servicio(models.Model):
    """"Modelo de servicios"""
    #id no es necesario colocarse, lo hace solo django
    fecha = models.DateTimeField()
    texto = models.CharField(max_length=240)
    comentario = models.CharField(max_length=240)
    puntuacion = models.IntegerField 
    costo = models.IntegerField 
    
class Tarea(models.Model):
    nombre = models.CharField(max_length=240)
    
class Estado(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=240)
    servicio = models.ManyToManyField(Servicio)
    fecha = models.DateTimeField()
