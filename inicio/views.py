from inicio.models import Producto
from django.shortcuts import render, redirect
from inicio.form import BuscarProductoFormulario, CrearProductoFormulario
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date

def inicio(request):
    return render(request, 'inicio/inicio.html')

def productos(request):
    return render(request, 'inicio/productos.html')

def acerca_de(request):
    return render(request, 'inicio/acerca_de.html')

@login_required
def crear_producto(request):

    if request.method == 'POST':
        formulario = CrearProductoFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data
            producto = Producto(
                nombre=info['nombre'],
                modelo=info['modelo'],
                precio=info['precio'],
                numero_telefono=info['numero_telefono'],
                autor=request.user.email,
                imagen=info['imagen'],
                fecha_creacion=date.today()
            )
            producto.save()
            return redirect('inicio:listar_productos')
        else:
            return render(request, 'inicio/crear_producto.html', {'formulario': formulario})

    formulario = CrearProductoFormulario()
    return render(request, 'inicio/crear_producto.html', {'formulario': formulario})

def listar_productos(request):
    formulario = BuscarProductoFormulario(request.GET)
    listado_de_productos = ""
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data['nombre']
    listado_de_productos = Producto.objects.filter(nombre__icontains=nombre_a_buscar)
    
    formulario = BuscarProductoFormulario()
    return render(request, 'inicio/listar_productos.html', {'formulario': formulario, 'productos': listado_de_productos, 'busqueda': nombre_a_buscar})


class ModificarProducto(LoginRequiredMixin, UpdateView):
    model = Producto
    template_name = 'inicio/modificar_producto.html'
    fields = ['nombre', 'modelo', 'precio', 'numero_telefono', 'imagen', 'descripcion']
    success_url = reverse_lazy('inicio:listar_productos')
    
class EliminarProducto(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = 'inicio/eliminar_producto.html'
    success_url = reverse_lazy('inicio:listar_productos')

class MostrarProducto(DetailView):
    model = Producto
    template_name = 'inicio/mostrar_producto.html'

