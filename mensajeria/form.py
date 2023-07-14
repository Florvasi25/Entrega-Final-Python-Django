from django import forms
from ckeditor.fields import RichTextFormField

class CrearMensajeFormulario(forms.Form):
    texto = RichTextFormField()
    destinatario = forms.CharField(max_length=20)

class BuscarMensajeFormulario(forms.Form):
    autor = forms.CharField(max_length=20, required=False)