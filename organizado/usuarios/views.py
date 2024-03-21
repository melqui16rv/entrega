from django.shortcuts import render, redirect
from django.http import HttpResponse

from oferta.forms import Actualizacion
from usuarios.forms import ImageForm
from .models import Usuario, Actualizar
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

def usuariolist(request):
    get_usuarios=Usuario.objects.all()
    data={
        'get_usuarios':get_usuarios
    }
    return render(request,'usuariolist.html',data)

def usuariolist(request):
    get_usuarios=Usuario.objects.all()
    data={
        'get_usuarios':get_usuarios
    }
    return render(request,'usuariolist.html',data)



#---------------------------------------------------------
def Image(request):
    if request.method == 'POST':
        form =ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponse('successfully uploaded')
    else:
        form = ImageForm()
    return render(request, "templates/candidato/postulacionesM", {"form": form})



#-------------------------------------------------------------------------

def editar(request,id_editar):
    actualizar=Actualizar.objects.filter(id=id_editar).first()
    form=Actualizacion(instance=actualizar)
    return render(request, "candidato/actualizarinfo.html",{"form":form,"actualizar":actualizar})

#-------------------------------------------------------------------------

def editar_perfil(request,id_editar):
    actualizar=Actualizar.objects.get(pk=id_editar)
    form=Actualizacion(request.POST,instance=actualizar)
    if form.is_valid():
       form.save()
       get_editar=Actualizar.objects.all()
       {"get_editar":get_editar}
    return render(request,"reclutador/postulacionesM.html")
    # return print("okey"),{"get_ofertas":get_ofertas}
    
#----------------------------------------------------------------------


def borrarinformacion(request, id_editar):
    edicion=Actualizar.objects.get(pk=id_editar)
    edicion.delete()
    editar=Actualizar.objects.all()
    return render(request, "usuariolist.html",{"get_editar":editar})

#-------------------------------------------------------------------------
