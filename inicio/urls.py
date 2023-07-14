from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('acerca-de', views.acerca_de, name='acerca_de'),
    path('productos/', views.productos, name='productos'),
    path('productos/lista/', views.listar_productos, name='listar_productos'),
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    path('productos/eliminar/<int:pk>/', views.EliminarProducto.as_view(), name='eliminar_producto'),
    path('productos/modificar/<int:pk>/', views.ModificarProducto.as_view(), name='modificar_producto'),
    path('productos/<int:pk>/', views.MostrarProducto.as_view(), name='mostrar_producto'),
]