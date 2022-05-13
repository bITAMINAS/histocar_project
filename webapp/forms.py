#################################################################
##################### Todo sobre formularios ####################
###### https://docs.djangoproject.com/en/3.0/ref/forms/api/ #####
#################################################################
#################################################################
from django import forms
from webapp.models import Servicio, Usuario, Vehiculo, Estado
from django.contrib.auth.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, Select, MultipleChoiceField, Textarea
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
        widgets = {
            'estados': SelectSingleAsList,
            'textoOtros': Textarea(attrs={'cols': 80, 'rows': 4}),
        }

class editarServicioForm(forms.ModelForm):
    
    estado = forms.ModelChoiceField(queryset=Estado.objects.all(), required=True, empty_label = None)
    class Meta:
        model = Servicio
        fields = ('fecha', 'textoOtros', 'kilometros', 'costo', 'vehiculo', 'tareas')
        widgets = { 
           # 'estados': SelectSingleAsList,
            'textoOtros': Textarea(attrs={'cols': 80, 'rows': 4}),
        }


class crearVehiculos(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ('modelo', 'color', 'nroChasis', 'matricula', 'anio', 'tipoCombustible', 'duenio')
        widgets = {
            'tipoCombustible': forms.RadioSelect(),
        }
    def __init__(self, *args, **kwargs):
        super(crearVehiculos, self).__init__(*args, **kwargs)
        self.fields['duenio'].queryset = Usuario.objects.filter(is_client=True)

class editarVehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ('__all__')
        widgets = {
            'tipoCombustible': forms.RadioSelect(),
        }

    def __init__(self, *args, **kwargs):
        super(editarVehiculoForm, self).__init__(*args, **kwargs)
        self.fields['duenio'].queryset = Usuario.objects.filter(is_client=True)
        

class crearVehiculosCliente(forms.ModelForm):
     class Meta:
        model = Vehiculo
        fields = ('modelo', 'color', 'nroChasis', 'matricula', 'anio', 'tipoCombustible')
        labels = {
            'nroChasis': _('Número de chasis'),
            'anio': _('Año'),
            'tipoCombustible': _('Combustible')
        }



class registroUsuario(UserCreationForm):
    error_css_class = 'form-control is-invalid'

    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    
    TIPOS_USUARIO = [('1', 'Cliente'), ('2', 'Empleado')]
    tipo_de_usuario = forms.ChoiceField(widget=forms.RadioSelect, choices=TIPOS_USUARIO,  initial='1')

    class Meta:
        model = Usuario
        fields = ('documento', 'email', 'telefono', 'nombre','dirDepartamento','dirCiudad', 'dirCalle', 'dirNumero', 'apellido', 'is_client', 'is_staff')
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'autocomplete': 'new-password'})

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
        fields = ['email', 'password']


class editarUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nombre', 'apellido', 'email', 'telefono','dirDepartamento','dirCiudad','dirCalle','dirNumero')
        labels = {
            'nombre': _('Nombre'),
            'apellido': _('Apellido'),
            'email': _('Email'),
            'telefono': _('Telefono'),
            'dirDepartamento': _('Departamento'),
            'dirCiudad': _('Ciudad'),
            'dirCalle': _('Calle'),
            'dirNumero': _('Numero'), 
        }

        
