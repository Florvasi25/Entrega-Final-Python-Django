from django import forms
from ckeditor.fields import RichTextFormField
from django.contrib.auth.models import User

class CrearMensajeFormulario(forms.Form):
    texto = RichTextFormField()
    destinatario = forms.ChoiceField(choices = [(x,x) for x in User.objects.values_list('username', flat=True)])
