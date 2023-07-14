from django.urls import path
from mensajeria import views

app_name = 'mensajeria'

urlpatterns = [
    # path('mensajes/', views.mensajes, name='mensajes'),
    path('mensajes/lista/', views.listar_mensajes, name='listar_mensajes'),
    path('mensajes/crear/', views.crear_mensaje, name='crear_mensaje'),
    # path('mensajes/eliminar/<int:pk>/', views.EliminarMensaje.as_view(), name='eliminar_mensaje'),
    # path('mensajes/modificar/<int:pk>/', views.ModificarMensaje.as_view(), name='modificar_mensaje'),
    # path('mensajes/<int:pk>/', views.MostrarMensaje.as_view(), name='mostrar_mensaje'),
]