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
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    tareas = models.ManyToManyField(Tarea)
    estados = models.ManyToManyField(Estados, through='Estado_Servicio')


class Tarea(models.Model):
    nombre = models.CharField(max_length=240)


class Estado(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=240)


# Relación N:N entre Estado<>Servicio
class Estado_Servicio(models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    fecha = models.DateField()


class Vehiculo(models.Model):
    Colors = models.TextChoices('Blanco', 'Rojo', 'Negro', 'Azul', 'Bordó', 'Marrón', 
                                'Gris Plata', 'Gris Ceniza', 'Amarillo', 'Verde', 'Otro')
    TiposCombustibles = models.TextChoices('Nafta', 'Gasoil', 'Híbrido', 'Eléctrico',
                                            'Hidrógeno', 'GLP')

    modelo = models.ForeignKey(Modelo) # Con el atributo modelo ya es suficiente, ya que a partir de él se puede inferir la Marca
    color = models.CharField(blank=True, choices=Colors.choices, max_length=15)
    nroChasis = models.CharField(max_length=50)
    matricula = models.CharField(max_length=50)
    anio = models.IntegerField 
    tipoCombustible = models.CharField(blank=True, choices=TiposCombustibles.choices, max_length=15)
    duenio = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class Marca(models.Model):
    nombre = models.CharField(max_length=20)


class Modelo(models.Model):
    nombre = models.CharField(max_length=20)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE) #Modelo pertenece a una Marca


class TipoCombustible(models.Model):
    nombre = models.CharField(max_length=20)

