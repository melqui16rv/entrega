from django.db import router
from django.urls import path, include
from . import views
from rest_framework import routers

urlpatterns = [
   
    path("inicio_Sesion_candidato/",views.regis_candidato, name="login_candidato"),
    path("",views.formulario, name="formulario"),
    path("", include(router.urls)),
]
