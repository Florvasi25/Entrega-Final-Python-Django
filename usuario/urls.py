from django.urls import path
from usuario import views
from django.contrib.auth.views import LogoutView

app_name = 'usuario'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(template_name='usuario/logout.html'), name='logout'),
    path('registro/', views.registrarse, name='registrarse'),
    path('perfil/mostrar/', views.mostrar_perfil, name='mostrar_perfil'),
    path('perfil/editar/', views.edicion_perfil, name='editar_perfil'),
    path('perfil/editar/password', views.ModificarPass.as_view(), name='modificar_pass'),
    path('perfil/editar/password/exito', views.exito_contra, name='exito_contra'),
]
