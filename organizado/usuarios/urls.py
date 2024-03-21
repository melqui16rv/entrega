from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
urlpatterns = [
    path('login/', views.login, name="select"),
    path('login_usurio', views.login_usurio, name="usuario"),
    path('login_empresa', views.login_empresa, name="empresa"),
    path('hoja_vida/', views.hoja_vida, name="hoja_vida"),
    path('inicio/', views.inicioC, name="inicioC"),
    path('inicio_/', views.inicioM, name="inicioM"),
    path('contacta/', views.contacta, name="contacta"),
    path('navegador/', views.navegador, name="navegador"),
    path('perfilC/', views.perfilC, name="perfilC"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('nosotrosC/', views.nosotrosC, name="nosotrosC"),
    
    path('registrarseC/', views.registrarseC, name="registrarseC"),
    path('registrarseM/', views.registrarseM, name="registrarseM"),
    
    path('usuarios/', views.usuarios, name="usuarios"),
    path('lista/', views.usuariolist, name="usuario_list"),
#-------------------------------------------------------------------------------------------------------------   

#----------------------------------------------------------------------------------------------------------------------------
    path('actualizar/<int:id_editar>/', views.editar, name="actualizacion"),
    path("editar/<int:id_editar>/", views.editar_perfil, name="editar"),
    path("eliminar/<int:id_editar>/", views.borrarinformacion, name="eliminar"),
    
    path('', include('oferta.urls')),
    path("", include(router.urls)),
]
