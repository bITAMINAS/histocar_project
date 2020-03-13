from django import forms
from webapp.models import Servicio, Usuario
from django.contrib.auth.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm
from django.forms import ModelForm, Select

class ServicioForm(forms.ModelForm):

    class Meta:
        model = Servicio
        fields = ('fecha', 'textoOtros', 'kilometros', 'costo', 'vehiculo',  'tareas',  'estados')
        widgets = {
            'estados': Select() label='Estado',
        }


# class CrearServicioForm(forms.Form):
#     name = forms.CharField(
#         label='Nombre',
#     )

#     email = forms.EmailField(
#         label='Correo electrónico',
#     )

#     message = forms.CharField(
#         label='Mensaje',
#         widget=forms.Textarea,
#     )



class registroUsuario(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('documento', 'email', 'telefono', 'nombre', 'apellido')