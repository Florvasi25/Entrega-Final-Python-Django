from django.shortcuts import render, redirect
from mensajeria.form import CrearMensajeFormulario, BuscarMensajeFormulario
from mensajeria.models import Mensaje
from datetime import date

# Create your views here.

def crear_mensaje(request):
    if request.method == 'POST':
        formulario = CrearMensajeFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data
            mensaje = Mensaje(
                texto=info['texto'],
                autor=request.user.email,
                destinatario=info['destinatario'],
                fecha_creacion=date.today()
            )
            mensaje.save()
            return redirect('mensajeria:listar_mensajes')
        else:
            return render(request, 'mensajeria/crear_mensaje.html', {'formulario': formulario})

    formulario = CrearMensajeFormulario()
    return render(request, 'mensajeria/crear_mensaje.html', {'formulario': formulario})

def listar_mensajes(request):
    formulario = BuscarMensajeFormulario(request.GET)
    listado_de_mensajes = ""
    if formulario.is_valid():
        mensaje_a_buscar = formulario.cleaned_data['autor']
    listado_de_mensajes = Mensaje.objects.filter(autor__icontains=mensaje_a_buscar)
    
    formulario = BuscarMensajeFormulario()
    return render(request, 'mensajeria/listar_mensajes.html', {'formulario': formulario, 'mensajes': listado_de_mensajes, 'busqueda': mensaje_a_buscar})

