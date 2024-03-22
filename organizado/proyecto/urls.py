"""
URL configuration for proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.db import router
from django.urls import path, include
from . import views
from . import settings
from django.conf.urls.static import static
from agendas.views import agenda_form, agenda_view
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from agendas.views import AgendaViewSet
from rest_framework.documentation import include_docs_urls


# router = DefaultRouter()
# router.register(r'agendas', AgendaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('',views.home,name="home"), 

    path('usuario/',include('usuarios.urls')),
    path('curriculum/', include('hojavida.urls')),
    path('agendas/',include('agendas.urls')),
    path('usuario/', include('usuarios.urls')),
    path('usuario/agenda_form/', agenda_form, name='agenda_form'),
    path('usuario/agenda/', agenda_view, name='agenda_view'),
    path("docs/", include_docs_urls(title="Api Documentation")),
    # path('api/', include(router.urls)),
    

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)