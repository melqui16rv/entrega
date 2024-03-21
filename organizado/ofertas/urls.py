from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'oferta', views.OfertaViewSet)

urlpatterns = [
    path('ofertas/', views.postulacionesM, name="postulacionesM"),
    path('postulaciones/', views.postulacionesC, name="postulacionesC"),
    path('formulario_ofertas/', views.formulario_ofertas, name='formulario_ofertas'),
    path('guardar_oferta/', views.guardar_oferta, name='guardar_oferta'),
    path('editarOfertas/<int:id_Ofertas>/', views.editarOfertas, name="editar_Ofertas"),
    path('actualizarOfertas/<int:id_Ofertas>/', views.actualizarOfertas, name='actualizar_Ofertas'),
    path("eliminarOferta/<int:id_Ofertas>",views.eliminarOferta, name="eliminar_Ofertas"),
    path("", include(router.urls)),
]
