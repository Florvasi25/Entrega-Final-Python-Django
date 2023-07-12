from django import forms

class UsuarioFormularioBase(forms.Form):
    nombre = forms.CharField(max_length=20) 
    edad = forms.IntegerField()
    email = forms.CharField(max_length=50) 
    numero_telefono = forms.IntegerField()
    
class CrearUsuarioFormulario(UsuarioFormularioBase):
    ...

class ModificarUsuarioFormulario(UsuarioFormularioBase):
    ...
class BuscarUsuarioFormulario(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)

# class BuscarProductoFormulario(forms.Form):
#     nombre = forms.CharField(max_length=20, required=False)
