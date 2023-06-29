from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('usuario/crear/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/lista', views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('productos/', views.productos, name='productos'),
]
