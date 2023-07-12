from inicio.models import Usuario
from django.shortcuts import render, redirect
from inicio.form import BuscarUsuarioFormulario
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

class CrearUsuario(CreateView):
    model = Usuario
    template_name = 'inicio/crear_usuario.html'
    fields = ['nombre', 'edad', 'email', 'numero_telefono', 'descripcion']
    success_url = reverse_lazy('inicio:listar_usuarios')

class ListarUsuarios(ListView):
    model = Usuario
    template_name = 'inicio/listar_usuarios.html'
    context_object_name = 'usuarios'

    def get_queryset(self):
        listado_de_usuarios = []
        formulario = BuscarUsuarioFormulario(self.request.GET)
        if formulario.is_valid():
            nombre_a_buscar = formulario.cleaned_data['nombre']
            listado_de_usuarios = Usuario.objects.filter(nombre__icontains=nombre_a_buscar)
        return listado_de_usuarios
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['formulario'] = BuscarUsuarioFormulario()
        return contexto

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

