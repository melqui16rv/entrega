from django.urls import path, include
from .views import hoja_vida_form, hoja_vida_view, llenarHojaVida, HojaVidaViewSet
from rest_framework import routers
from django.contrib import admin


router = routers.DefaultRouter()
router.register(r'hova_vida', HojaVidaViewSet)

urlpatterns = [
    path('hoja_vida_form/', hoja_vida_form, name='hoja_vida_form'),
    path('hoja_vida/', hoja_vida_view, name='hoja_vida'),
    path('llenarHojaVida/', llenarHojaVida, name='llenarHojaVida'),
    path("", include(router.urls)),
    path('admin/', admin.site.urls),
    path('usuario/', include('usuarios.urls')),
]