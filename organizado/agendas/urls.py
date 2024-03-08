from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from .views import AgendaViewSet
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'lista', views.AgendaViewSet)

urlpatterns = [
    path('formulario_agenda/', views.formulario_agenda, name='formulario_agenda'),
    path('llenar_formulario_agenda/', views.llenar_formulario_agenda, name='llenar_formulario_agenda'),
    path('agenda/', views.agenda, name='agenda'),
    path('editar_agenda/<int:agenda_id>/', views.editar_agenda, name='editar_agenda'),
    path('eliminar_agenda/<int:agenda_id>/', views.eliminar_agenda, name='eliminar_agenda'),
    path('', include(router.urls)),
]