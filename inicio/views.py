from inicio.models import Usuario
from django.shortcuts import render, redirect
from inicio.form import BuscarUsuarioFormulario, CrearUsuarioFormulario
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
    return render(request, 'inicio/inicio.html')

def usuarios(request):
    return render(request, 'inicio/usuarios.html')

def acerca_de(request):
    return render(request, 'inicio/acerca_de.html')

def crear_usuario(request):

    if request.method == 'POST':
        formulario = CrearUsuarioFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            usuario = Usuario(nombre=info['nombre'], edad=info['edad'], email=info['email'], numero_telefono=info['numero_telefono'], autor=request.user.email)
            usuario.save()
            return redirect('inicio:listar_usuarios')
        else:
            return render(request, 'inicio/crear_usuario.html', {'formulario': formulario})

    formulario = CrearUsuarioFormulario()
    return render(request, 'inicio/crear_usuario.html', {'formulario': formulario})

def listar_usuarios(request):
    formulario = BuscarUsuarioFormulario(request.GET)
    listado_de_usuarios = ""
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data['nombre']
    listado_de_usuarios = Usuario.objects.filter(nombre__icontains=nombre_a_buscar)
    
    formulario = BuscarUsuarioFormulario()
    return render(request, 'inicio/listar_usuarios.html', {'formulario': formulario, 'usuarios': listado_de_usuarios, 'busqueda': nombre_a_buscar})


class ModificarUsuario(LoginRequiredMixin, UpdateView):
    model = Usuario
    template_name = 'inicio/modificar_usuario.html'
    fields = ['nombre', 'edad', 'email', 'numero_telefono', 'descripcion']
    success_url = reverse_lazy('inicio:listar_usuarios')
    
class EliminarUsuario(LoginRequiredMixin, DeleteView):
    model = Usuario
    template_name = 'inicio/eliminar_usuario.html'
    success_url = reverse_lazy('inicio:listar_usuarios')

class MostrarUsuario(DetailView):
    model = Usuario
    template_name = 'inicio/mostrar_usuario.html'

