from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, AuthenticationForm
from django.contrib.auth.models import User

class MiFormularioDeCreacionDeUsuario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class MiFormularioDeEdicionDeDatosDeUsuario(UserChangeForm):
    password = None
    first_name = forms.CharField(label='Nombre', max_length=20, required=False)
    last_name = forms.CharField(label='Apellido', max_length=20, required=False)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar']

class MiFormularioCambioContrasenia(PasswordChangeForm):
    old_password = forms.CharField(label='Contraseña Anterior', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='Nueva Contraseña', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Confirme Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {k:"" for k in fields}

class MiFormularioLogin(AuthenticationForm):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    
