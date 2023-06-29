from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from inicio.models import Usuario
from django.shortcuts import render, redirect
from inicio.form import CrearUsuarioFormulario, BuscarUsuarioFormulario

def inicio(request):
    return render(request, 'inicio/inicio.html')

def crear_usuario(request):

    if request.method == 'POST':
        formulario = CrearUsuarioFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            usuario = Usuario(nombre=info['nombre'], edad=info['edad'], email=info['email'], numero_telefono=info['numero_telefono'])
            usuario.save()
            return redirect('inicio:listar_usuarios')
        else:
            return render(request, 'inicio/crear_usuarios.html', {'formulario': formulario})

    formulario = CrearUsuarioFormulario()
    return render(request, 'inicio/crear_usuarios.html', {'formulario': formulario})

def listar_usuarios(request):
    formulario = BuscarUsuarioFormulario(request.GET)
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data['nombre']
    listado_de_usuarios = Usuario.objects.filter(nombre__icontains=nombre_a_buscar)
    
    formulario = BuscarUsuarioFormulario()
    return render(request, 'inicio/listar_usuarios.html', {'formulario': formulario, 'usuarios': listado_de_usuarios, 'busqueda': nombre_a_buscar})