from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from .views import AgendaViewSet
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'lista', views.AgendaViewSet)

urlpatterns = [
    path('formulario_agenda/', views.formulario_agendaC, name='formulario_agendaC'),
    path('formulario_agenda/', views.formulario_agendaM, name='formulario_agendaM'),
    path('llenar_formulario_agenda/', views.llenar_formulario_agendaC, name='llenar_formulario_agendaC'),
    path('llenar_formulario_agenda/', views.llenar_formulario_agendaM, name='llenar_formulario_agendaM'),
    path('usuario=id', views.agendaC, name='agendaC'),
    path('', views.agendaM, name='agendaM'),
    path('editar_agenda/<int:agenda_id>/', views.editar_agendaC, name='editar_agendaC'),
    path('editar_agenda/<int:agenda_id>/', views.editar_agendaM, name='editar_agendaM'),
    path('eliminar_agenda/<int:agenda_id>/', views.eliminar_agendaC, name='eliminar_agendaC'),
    path('eliminar_agenda/<int:agenda_id>/', views.eliminar_agendaM, name='eliminar_agendaM'),
    path('', include(router.urls)),
]