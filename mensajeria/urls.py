from django.urls import path
from mensajeria import views

app_name = 'mensajeria'

urlpatterns = [
    path('mensajes/lista/', views.listar_mensajes, name='listar_mensajes'),
    path('mensajes/crear/', views.crear_mensaje, name='crear_mensaje'),
]