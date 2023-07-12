from typing import Any, Dict
from django.db.models.query import QuerySet
from inicio.models import Usuario
from django.shortcuts import render, redirect
from inicio.form import CrearUsuarioFormulario, BuscarUsuarioFormulario, ModificarUsuarioFormulario
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
    return render(request, 'inicio/inicio.html')

# def crear_usuario(request):

#     if request.method == 'POST':
#         formulario = CrearUsuarioFormulario(request.POST)
#         if formulario.is_valid():
#             info = formulario.cleaned_data
#             usuario = Usuario(nombre=info['nombre'], edad=info['edad'], email=info['email'], numero_telefono=info['numero_telefono'])
#             usuario.save()
#         else:
#             return render(request, 'inicio/crear_usuarios.html', {'formulario': formulario})

#     formulario = CrearUsuarioFormulario()
#     return render(request, 'inicio/crear_usuarios.html', {'formulario': formulario})

# def listar_usuarios(request):
#     formulario = BuscarUsuarioFormulario(request.GET)
#     listado_de_usuarios = ""
#     if formulario.is_valid():
#         nombre_a_buscar = formulario.cleaned_data['nombre']
#     listado_de_usuarios = Usuario.objects.filter(nombre__icontains=nombre_a_buscar)
    
#     formulario = BuscarUsuarioFormulario()
#     return render(request, 'inicio/listar_usuarios.html', {'formulario': formulario, 'usuarios': listado_de_usuarios, 'busqueda': nombre_a_buscar})

def usuarios(request):
    return render(request, 'inicio/usuarios.html')

# def productos(request):
#     formulario_productos = BuscarProductoFormulario(request.GET)
#     if formulario_productos.is_valid():
#         producto_a_buscar = formulario_productos.cleaned_data['nombre']
#     listado_de_productos = Productos.objects.filter(nombre__icontains=producto_a_buscar)
    
#     formulario_productos = BuscarProductoFormulario()
#     return render(request, 'inicio/productos.html', {'formulario_productos': formulario_productos, 'productos': listado_de_productos, 'busqueda_producto': producto_a_buscar})

# def eliminar_usuario(request, usuario_id):
#     usuario = Usuario.objects.get(id=usuario_id)
#     usuario.delete()

#     return redirect('inicio:listar_usuarios')

# def modificar_usuario(request, usuario_id):
#     usuario_a_modificar = Usuario.objects.get(id=usuario_id)

#     if request.method == 'POST':
#         formulario = ModificarUsuarioFormulario(request.POST)
#         if formulario.is_valid():
#             info = formulario.cleaned_data
#             usuario_a_modificar.nombre = info['nombre']
#             usuario_a_modificar.edad = info['edad']
#             usuario_a_modificar.email = info['email']
#             usuario_a_modificar.numero_telefono = info['numero_telefono']
#             usuario_a_modificar.save()
#             return redirect('inicio:listar_usuarios')
#         else:
#             return  render(request, 'inicio/modificar_usuario.html', {'formulario': formulario})
    
#     formulario = ModificarUsuarioFormulario(initial={'nombre': usuario_a_modificar.nombre, 'edad': usuario_a_modificar.edad, 'email': usuario_a_modificar.email, 'numero_telefono': usuario_a_modificar.numero_telefono})
#     return render(request, 'inicio/modificar_usuario.html', {'formulario': formulario})

#CBV

class CrearUsuario(CreateView):
    model = Usuario
    template_name = 'inicio/CBV/crear_usuario_CBV.html'
    fields = ['nombre', 'edad', 'email', 'numero_telefono', 'descripcion']
    success_url = reverse_lazy('inicio:listar_usuarios')

class ListarUsuarios(ListView):
    model = Usuario
    template_name = 'inicio/CBV/listar_usuarios_CBV.html'
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
    template_name = 'inicio/CBV/modificar_usuario_CBV.html'
    fields = ['nombre', 'edad', 'email', 'numero_telefono', 'descripcion']
    success_url = reverse_lazy('inicio:listar_usuarios')
    
class EliminarUsuario(LoginRequiredMixin, DeleteView):
    model = Usuario
    template_name = 'inicio/CBV/eliminar_usuario_CBV.html'
    success_url = reverse_lazy('inicio:listar_usuarios')

class MostrarUsuario(DetailView):
    model = Usuario
    template_name = 'inicio/CBV/mostrar_usuario_CBV.html'

