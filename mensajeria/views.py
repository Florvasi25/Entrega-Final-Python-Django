from django.shortcuts import render, redirect
from mensajeria.form import CrearMensajeFormulario
from mensajeria.models import Mensaje
from django.contrib.auth.decorators import login_required
from datetime import date

# Create your views here.

@login_required
def crear_mensaje(request):
    if request.method == 'POST':
        formulario = CrearMensajeFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data
            mensaje = Mensaje(
                texto=info['texto'],
                autor=request.user.username,
                destinatario=info['destinatario'],
                fecha_creacion=date.today()
            )
            mensaje.save()
            return redirect('mensajeria:listar_mensajes')
        else:
            return render(request, 'mensajeria/crear_mensaje.html', {'formulario': formulario})

    formulario = CrearMensajeFormulario()
    return render(request, 'mensajeria/crear_mensaje.html', {'formulario': formulario})

@login_required
def listar_mensajes(request):
    mensajes_recibidos = Mensaje.objects.filter(destinatario=request.user.username)
    mensajes_enviados = Mensaje.objects.filter(autor=request.user.username)
    
    return render(request, 'mensajeria/listar_mensajes.html', {'mensajes_recibidos': mensajes_recibidos, 'mensajes_enviados': mensajes_enviados})

