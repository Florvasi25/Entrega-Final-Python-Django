from django import forms

class BuscarUsuarioFormulario(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
