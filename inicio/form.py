from django import forms

class CrearProductoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20) 
    modelo = forms.CharField(max_length=20) 
    precio = forms.IntegerField()
    numero_telefono = forms.IntegerField(label='Número de Contacto')
    imagen = forms.ImageField()

class BuscarProductoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
