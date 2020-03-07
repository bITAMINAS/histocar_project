from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=20, default="")
    apellido = models.CharField(max_length=20, default="")
    documento = models.CharField(max_length=8, default="")
    email = models.EmailField(unique=True, default="") #unique=True sirve para que no se repita en la bd
    telefono = models.CharField(max_length=20, default="")
    tipoUsuario = models.IntegerField(default=0)
    dirDepartamento = models.CharField('Departamento',max_length=20, default="")
    dirCiudad = models.CharField(max_length=20, default="")
    dirCalle = models.CharField(max_length=50, default="")
    dirNumero = models.CharField(max_length=5, default="")

    def __str__(self):
        return self.nombre + ' ' + self.apellido
    
class Servicio(models.Model):
    fecha = models.DateTimeField()
    textoOtros = models.CharField(max_length=240, default="")
    comentario = models.CharField(max_length=240, default="")
    kilometros = models.IntegerField(default=0)
    puntuacion = models.IntegerField(default=0)
    costo = models.IntegerField(default=0)
    vehiculo = models.ForeignKey('Vehiculo', on_delete=models.CASCADE, default="")
    tareas = models.ManyToManyField('Tarea')
    estados = models.ManyToManyField('Estado', through='Estado_Servicio')

class Tarea(models.Model):
    nombre = models.CharField(max_length=240, default="")

class Estado(models.Model):
    nombre = models.CharField(max_length=50, default="")
    descripcion = models.CharField(max_length=240, default="")

# Relación N:N entre Estado<>Servicio
class Estado_Servicio(models.Model):
    servicio = models.ForeignKey('Servicio', on_delete=models.CASCADE)
    estado = models.ForeignKey('Estado', on_delete=models.CASCADE)
    fecha = models.DateField()

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
        return self.modelo

class Marca(models.Model):
    nombre = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.nombre

class Modelo(models.Model):
    nombre = models.CharField(max_length=20, default="")
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE) #Modelo pertenece a una Marca
