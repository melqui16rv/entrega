from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'oferta', views.OfertaViewSet)

urlpatterns = [
    path('login/', views.login, name="select"),
    path('login_usurio', views.login_usurio, name="usuario"),
    path('login_empresa', views.login_empresa, name="empresa"),
    path('hoja_vida/', views.hoja_vida, name="hoja_vida"),
    path('notificaciones=id/', views.notificacionesC, name="notificacionesC"),
    path('notificaciones/', views.notificacionesM, name="notificacionesM"),
    path('contacta/', views.contacta, name="contacta"),
    path('navegador/', views.navegador, name="navegador"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('usuarios/', views.usuarios, name="usuarios"),
    path('lista/', views.usuariolist, name="usuario_list"),
    path('ofertas/', views.postulacionesM, name="postulacionesM"),
    path('postulaciones/', views.postulacionesC, name="postulacionesC"),
    path('formulario_ofertas/', views.formulario_ofertas, name='formulario_ofertas'),
    path('guardar_oferta/', views.guardar_oferta, name='guardar_oferta'),
    path('editarOfertas/<int:id_Ofertas>/', views.editarOfertas, name="editar_Ofertas"),
    path('actualizarOfertas/<int:id_Ofertas>/', views.actualizarOfertas, name='actualizar_Ofertas'),
    
    
    
    
    path("eliminarOferta/<int:id_Ofertas>",views.eliminarOferta, name="eliminar_Ofertas"),
    
    
    
    
    
    
    
    
    
    path('actua/', views.formulario_actualizacion, name='actualizar'),
#-------------------------------------------------------------------------------------------------------------   

#----------------------------------------------------------------------------------------------------------------------------
    path('actualizar/<int:id_editar>/', views.editar, name="actualizacion"),
    path("editar/<int:id_editar>/", views.editar_perfil, name="editar"),
    path("eliminar/<int:id_editar>/", views.borrarinformacion, name="eliminar"),
    

    path("", include(router.urls)),
]
