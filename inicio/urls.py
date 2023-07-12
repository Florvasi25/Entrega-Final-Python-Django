from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('usuarios/', views.usuarios, name='usuarios'),
    # path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    # path('usuarios/lista/', views.listar_usuarios, name='listar_usuarios'),
    # path('usuarios/eliminar/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),
    # path('usuarios/modificar/<int:usuario_id>/', views.modificar_usuario, name='modificar_usuario'),

    #CBV
    path('usuarios/lista/', views.ListarUsuarios.as_view(), name='listar_usuarios'),
    path('usuarios/crear/', views.CrearUsuario.as_view(), name='crear_usuario'),
    path('usuarios/eliminar/<int:pk>/', views.EliminarUsuario.as_view(), name='eliminar_usuario'),
    path('usuarios/modificar/<int:pk>/', views.ModificarUsuario.as_view(), name='modificar_usuario'),
    path('usuarios/<int:pk>/', views.MostrarUsuario.as_view(), name='mostrar_usuario'),
]