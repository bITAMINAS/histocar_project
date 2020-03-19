#################################################################
##################### Todo sobre formularios ####################
###### https://docs.djangoproject.com/en/3.0/ref/forms/api/ #####
#################################################################
#################################################################
from django import forms
from webapp.models import Servicio, Usuario, Vehiculo
from django.contrib.auth.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, Select, MultipleChoiceField
from django.utils.datastructures import MultiValueDict

################################################################################

#fix bug 10 https://stackoverflow.com/questions/14969969/django-representing-user-groups-manytomanyfield-as-a-select-in-form
class SelectSingleAsList(Select):
    def value_from_datadict(self, data, files, name):
        if isinstance(data, (MultiValueDict)):
            return data.getlist(name)  # NOTE this returns a list rather than a single value.
        return data.get(name, None)

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ('fecha', 'textoOtros', 'kilometros', 'costo', 'vehiculo',  'tareas',  'estados')
        widgets = { 'estados': SelectSingleAsList,}

class editarServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ('fecha', 'textoOtros', 'kilometros', 'costo', 'vehiculo',  'tareas',  'estados')
        widgets = { 'estados': SelectSingleAsList,}
        

class crearVehiculos(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ('modelo', 'color', 'nroChasis', 'matricula', 'anio', 'tipoCombustible', 'duenio')
        labels = {
            'duenio': _('Propietario'),
            'nroChasis': _('Número de chasis'),
            'anio': _('Año'),
            'tipoCombustible': _('Combustible')
        }



class registroUsuario(UserCreationForm):
    error_css_class = 'form-control is-invalid'

    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('documento', 'email', 'telefono', 'nombre', 'apellido')
        labels = {
            'documento': _('Cédula de identidad'),
        }
        help_texts = {
            'documento': _('Sin puntos ni guiones, 8 carcateres'),
            'password1': _('No puede ser sólo números'),
        }
        error_messages = {
            'documento': {
                'max_length': _("Largo excedido, máximo 8 caracteres."),
            },
        }

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user



class Login(forms.Form): # Note: forms.Form NOT forms.ModelForm
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control','type':'text','name': 'username', 'autofoucs':'autofocus'}), 
        label='Documento de identidad')
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control','type':'password', 'name': 'password'}),
        label='Password')

    class Meta:
        fields = ['username', 'password']
