from django import forms
from webapp.models import Servicio, Usuario
from django.contrib.auth.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ('fecha', 'textoOtros', 'kilometros', 'costo', 'vehiculo',  'tareas',  'estados')

class registroUsuario(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('documento', 'email', 'telefono', 'nombre', 'apellido')