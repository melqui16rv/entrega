from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'oferta', views.OfertaViewSet)

urlpatterns = [
    path('ofertas/', views.postulacionesM, name="postulacionesM"),
    path('postulaciones/', views.postulacionesC, name="postulacionesC"),
    path('formulario_ofertas/', views.formulario_oferta, name='formulario_oferta'),
    path('guardar_oferta/', views.guardar_oferta, name='guardar_oferta'),
    path('editarOferta/<int:id_Oferta>/', views.editarOferta, name="editar_Oferta"),
    path('actualizarOferta/<int:id_Oferta>/', views.actualizarOferta, name='actualizar_Oferta'),
    path("eliminarOferta/<int:id_Oferta>",views.eliminarOferta, name="eliminar_Oferta"),

    path("", include(router.urls)),
]
