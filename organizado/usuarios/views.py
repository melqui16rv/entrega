from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario, Actualizar
from .forms import ImageForm 
from rest_framework import viewsets
# from .forms import FormularioAgendaForm
# from .forms import AgendaForm

def login(request):
    return render(request,'login/select.html')

def login_usurio(request):
    return render(request,'login/usuario.html')

def login_empresa(request):
    return render(request,'login/empresa.html')



def hoja_vida(request):
    return render(request,'candidato/hoja_vida.html')

def inicioC(request):
    return render(request,'candidato/inicioC.html')
def nosotrosC(request):
    return render(request,'candidato/nosotrosC.html')


def inicioM(request):
    return render(request,'reclutador/inicioM.html')
def nosotrosM(request):
    return render(request,'reclutador/nosotrosM.html')


def perfilC(request):
    return render(request,'candidato/perfilC.html')

def registrarseC(request):
    return render(request,'login/registrarseC.html')

def registrarseM(request):
    return render(request,'login/registrarseM.html')



def navegador(request):
    return render(request,'pag/navegador.html')

def contacta(request):
    return render(request,'pag/contacta.html')

def nosotros(request):
    return render(request,'pag/nosotros.html')

def usuarios(request):
    return render(request,'usuariolist.html')