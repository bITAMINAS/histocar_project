from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=20, default="")
    apellido = models.CharField(max_length=20, default="")
    documento = models.CharField(max_length=8, default="")
    email = models.EmailField(unique=True, default="") #unique=True sirve para que no se repita en la bd
    telefono = models.CharField(max_length=20, default="")
    tipoUsuario = models.IntegerField(default=0)
    dirDepartamento = models.CharField(max_length=20, default="")
    dirCiudad = models.CharField(max_length=20, default="")
    dirCalle = models.CharField(max_length=50, default="")
    dirNumero = models.CharField(max_length=5, default="")
    
class Servicio(models.Model):
    fecha = models.DateTimeField()
    textoOtros = models.CharField(max_length=240, default="")
    comentario = models.CharField(max_length=240, default="")
    kilometros = models.IntegerField 
    puntuacion = models.IntegerField 
    costo = models.IntegerField 
    vehiculo = models.ForeignKey('Vehiculo', on_delete=models.CASCADE, default='1')
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
    TiposCombustibles = models.TextChoices('Combustibles', 'Nafta Gasoil Híbrido Eléctrico Hidrógeno GLP')
    Colores = models.TextChoices('Color', 'Blanco Rojo Negro Azul Bordó Marrón Gris_Plata Gris_Ceniza Amarillo Verde Otro')
    #Para probar que esta opcion funciona: Abre una consola y pone
    #python
    #from django.db import models
    #Colores = models.TextChoices('Color', 'Blanco Rojo Negro Azul Bordó Marrón Gris_Plata')
    #Colores.choices
    # Deberia devovler: [('Blanco', 'Blanco'), ('Rojo', 'Rojo'), ('Negro', 'Negro'), ('Azul', 'Azul'), ('Bordó', 'Bordó'), ('Marrón', 'Marrón'), ('Gris_Plata', 'Gris Plata')]
    #saludos
    modelo = models.ForeignKey('Modelo', on_delete=models.CASCADE) # Con el atributo modelo ya es suficiente, ya que a partir de él se puede inferir la Marca
    color = models.CharField(blank=True, choices=Colores.choices, max_length=15)
    nroChasis = models.CharField(max_length=50, default="")
    matricula = models.CharField(max_length=50, default="")
    anio = models.IntegerField 
    tipoCombustible = models.CharField(blank=True, choices=TiposCombustibles.choices, max_length=15)
    duenio = models.ForeignKey('Usuario', on_delete=models.CASCADE)

class Marca(models.Model):
    nombre = models.CharField(max_length=20, default="")

class Modelo(models.Model):
    nombre = models.CharField(max_length=20, default="")
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE) #Modelo pertenece a una Marca

class TipoCombustible(models.Model):
    nombre = models.CharField(max_length=20, default="")