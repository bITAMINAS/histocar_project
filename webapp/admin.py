from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

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
admin.site.register(Servicio)
admin.site.register(Tarea)
admin.site.register(Estado)
admin.site.register(Vehiculo)
admin.site.register(Marca)
admin.site.register(Modelo)


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('documento', 'password', 'email', 'telefono', 'is_active', 'is_admin', 'dirDepartamento', 'dirCiudad', 'dirCalle', 'dirNumero')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Usuario
        fields = ('documento', 'password', 'email', 'telefono', 'is_active', 'is_admin', 'dirDepartamento', 'dirCiudad', 'dirCalle', 'dirNumero')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('documento', 'email', 'nombre', 'apellido', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('documento', 'password')}),
        ('Info personal', {'fields': ('email','nombre', 'apellido', 'telefono')}),
        ('Ubicacion', {'fields': ('dirDepartamento', 'dirCiudad', 'dirCalle', 'dirNumero')}),
        ('Permisos', {'fields': ('is_admin', 'is_staff', 'tipoUsuario')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('documento', 'email', 'password1', 'password2', 'nombre', 'apellido', 'telefono','dirDepartamento', 'dirCiudad', 'dirCalle', 'dirNumero'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(Usuario, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)