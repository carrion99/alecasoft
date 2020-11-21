from django import forms
from django.forms import *
from core.erp.models import *

class CiudadForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['idCiudad'].widget.attrs['autofocus'] = True
    class Meta:
        model = Ciudad
        fields = '__all__'
        labels ={
            'idCiudad': 'Id',
            'ciudad': 'Ciudad',
            'descripcion': 'Descripcion'
        }
        widgets = {
            'idCiudad': NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un id'
                }
            ),
            'ciudad': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una ciudad'
                }
            ),
            'descripcion': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una descripcion',
                    'rows': 3,
                    'cols': 3
                }
            )
        }

class UsuarioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['idUsuario'].widget.attrs['autofocus'] = True
    class Meta:
        model = Usuario
        fields = '__all__'
        labels ={
            'idUsuario': 'Id',
            'nombreUsuario': 'Usuario',
            'claveUsuario': 'Contraseña'
        }
        widgets = {
            'idUsuario': NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un id'
                }
            ),
            'nombreUsuario': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un usuario'
                }
            ),
            'claveUsuario': PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una contraseña'
                }
            )
        }

class Estado_CivilForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['idEstadoCivil'].widget.attrs['autofocus'] = True

    class Meta:
        model = Estado_Civil
        fields = '__all__'
        labels = {
            'idEstadoCivil': 'Id',
            'estadoCivil': 'Estado Civil',
            'descripcion': 'Descripcion'
        }
        widgets = {
            'idEstadoCivil': NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un id'
                }
            ),
            'estadoCivil': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un usuario'
                }
            ),
            'descripcion': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una contraseña',
                    'rows': 3,
                    'cols': 3
                }
            )
        }

class DireccionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['idDireccion'].widget.attrs['autofocus'] = True

    class Meta:
        model = Direccion
        fields = '__all__'
        labels = {
            'idDireccion': 'Id',
            'callePrincipal': 'Calle Principal',
            'calleSecundaria': 'Calle Secundaria',
            'referencia': 'Referencia',
            'descripcion': 'Descripcion'
        }
        widgets = {
            'idDireccion': NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un id'
                }
            ),
            'callePrincipal': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese calle principal'
                }
            ),
            'calleSecundaria': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese calle secundaria'
                }
            ),
            'referencia': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una referencia'
                }
            ),
            'descripcion': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una descripcion',
                    'rows': 3,
                    'cols': 3
                }
            )
        }

class TelefonoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['idTelefono'].widget.attrs['autofocus'] = True

    class Meta:
        model = Telefono
        fields = '__all__'
        labels = {
            'idTelefono': 'Id',
            'numero': 'Telefono',
            'descripcion': 'Descripcion'
        }
        widgets = {
            'idTelefono': NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un id'
                }
            ),
            'numero': NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese numero de telefono'
                }
            ),
            'descripcion': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una descripcion',
                    'rows': 3,
                    'cols': 3
                }
            )
        }

class TipoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['idTipo'].widget.attrs['autofocus'] = True

    class Meta:
        model = Tipo
        fields = '__all__'
        labels = {
            'idTipo': 'Id',
            'tipo': 'Profesion',
            'descripcion': 'Descripcion'
        }
        widgets = {
            'idTipo': NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un id'
                }
            ),
            'tipo': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese nombre de profesion'
                }
            ),
            'descripcion': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una descripcion',
                    'rows': 3,
                    'cols': 3
                }
            )
        }

class EmailForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['idEmail'].widget.attrs['autofocus'] = True

    class Meta:
        model = Email
        fields = '__all__'
        labels = {
            'idEmail': 'Id',
            'email': 'E-mail',
            'descripcion': 'Descripcion'
        }
        widgets = {
            'idEmail': NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un id'
                }
            ),
            'email': EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un correo electronico'
                }
            ),
            'descripcion': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una descripcion',
                    'rows': 3,
                    'cols': 3
                }
            )
        }

class GeneroForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['idSexo'].widget.attrs['autofocus'] = True

    class Meta:
        model = Sexo
        fields = '__all__'
        labels = {
            'idSexo': 'Id',
            'sexo': 'Genero',
            'descripcion': 'Descripcion'
        }
        widgets = {
            'idSexo': NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un id'
                }
            ),
            'sexo': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un correo electronico'
                }
            ),
            'descripcion': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una descripcion',
                    'rows': 3,
                    'cols': 3
                }
            )
        }

class PersonaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['dni'].widget.attrs['autofocus'] = True

    class Meta:
        model = Persona
        fields = '__all__'
        labels = {
            'dni': 'Dni',
            'Tipo': 'Profesion',
            'apellidoPaterno': 'Apellido Paterno',
            'apellidoMaterno': 'Apellido Materno',
            'nombres': 'Nombres',
            'fechaNacimiento': 'Fecha Nacimiento (dd/mm/yyyy)',
            'Sexo': 'Genero',
            'Estado_Civil': 'Estado civil',
            'Ciudad': 'Ciudad',
            'Direccion': 'Direccion',
            'Email': 'Email',
            'Usuario': 'Usuario'
        }
        widgets = {
            'dni': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese numero de cedula'
                }
            ),
            'Tipo': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'apellidoPaterno': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese apellido paterno'
                }
            ),
            'apellidoMaterno': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese apellido materno'
                }
            ),
            'nombres': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese nombres'
                }
            ),
            'fechaNacimiento': DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '(dd/mm/yyyy)'
                }
            ),
            'Sexo': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'Estado_Civil': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'Ciudad': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'Direccion': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'Email': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'Usuario': Select(
                attrs={
                    'class': 'form-control'
                }
            )
        }

