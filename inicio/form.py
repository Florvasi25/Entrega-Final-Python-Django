from django import forms

class CrearUsuarioFormulario(forms.Form):
    nombre = forms.CharField(max_length=20) 
    edad = forms.IntegerField()
    email = forms.CharField(max_length=50) 
    numero_telefono = forms.IntegerField()

class BuscarUsuarioFormulario(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)

class BuscarProductoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
