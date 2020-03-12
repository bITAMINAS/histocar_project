from django import forms
from .models import Servicio

class ServicioForm(forms.ModelForm):

    class Meta:
        model = Servicio
        fields = ('fecha', 'textoOtros', 'kilometros', 'costo', 'vehiculo',  'tareas',  'estados')