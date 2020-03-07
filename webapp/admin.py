from django.contrib import admin

# Register your models here.
# the module name is app_name.models
from webapp.models import Usuario
from webapp.models import Servicio
from webapp.models import Tarea
from webapp.models import Estado
from webapp.models import Vehiculo
from webapp.models import Marca
from webapp.models import Modelo



# Register your models to admin site, then you can add, edit, delete and search your models in Django admin site.
admin.site.register(Usuario)
admin.site.register(Servicio)
admin.site.register(Tarea)
admin.site.register(Estado)
admin.site.register(Vehiculo)
admin.site.register(Marca)
admin.site.register(Modelo)
