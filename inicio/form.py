from django import forms
from ckeditor.fields import RichTextFormField

class CrearProductoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50) 
    modelo = forms.CharField(max_length=50, required=False) 
    precio = forms.IntegerField()
    descripcion = RichTextFormField(required=False)
    numero_telefono = forms.IntegerField(label='Número de Contacto')
    imagen = forms.ImageField()

class BuscarProductoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
