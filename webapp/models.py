from django.db import models

# Create your models here.

class Usuario(models.Model):
    id
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    documento = models.CharField(max_length=8)
    email = models.EmailField
    telefono = models.CharField(max_length=20)
    tipoUsuario = models.IntegerField(default=0)
    direccion = models.CharField(max_length=200)


