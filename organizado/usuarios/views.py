from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Ofertas, Usuario, Actualizar
from .forms import OfertaForm, ImageForm , Actualizacion
from rest_framework import viewsets
from .serializer import OfertaSerializer
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

def notificacionesM(request):
    return render(request,'reclutador/notificacionesM.html')

def notificacionesC(request):
    return render(request,'candidato/notificacionesC.html')

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
def postulacionesM(request):
    data = Ofertas.objects.all()
    return render(request, 'reclutador/postulacionesM.html', {'ofertas': data})

def postulacionesC(request):
    data = Ofertas.objects.all()
    return render(request, 'candidato/postulacionesC.html', {'ofertas': data})


#---------------------------------------------------------
def guardar_oferta(request):
    if request.method == 'POST':
        form = OfertaForm(request.POST)
        if form.is_valid():
            
            form.save()
            return redirect('reclutador/formulario_ofertas')
    else:
        form = OfertaForm()

    context = {'form': form}
    return render(request, 'reclutador/formulario_ofertas.html', context)


#---------------------------------------------------------
def formulario_ofertas(request):
    if request.method == 'POST':
        form = OfertaForm(request.POST)
        if form.is_valid():
       
            form.save()
            return redirect('formulario_ofertas')  
    else:
        form = OfertaForm()


    context = {'form': form}
    return render(request, 'reclutador/formulario_ofertas.html', context)


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



#---------------------------------------------------------
def editarOfertas(request,id_Ofertas):
    oferta=Ofertas.objects.filter(id=id_Ofertas).first()
    form=OfertaForm(instance=oferta)
    return render(request, "reclutador/editarOfertas.html",{"form":form,"oferta":oferta})

#---------------------------------------------------------
def actualizarOfertas(request,id_Ofertas):
    oferta=Ofertas.objects.get(pk=id_Ofertas)
    form=OfertaForm(request.POST,instance=oferta)
    if form.is_valid():
       form.save()
       get_ofertas=Ofertas.objects.all()
       {"get_ofertas":get_ofertas}
    return render(request,"reclutador/postulacionesM.html")
    # return print("okey"),{"get_ofertas":get_ofertas}











    
    
    
    
    
    
    
    
    

#------------------------------------------------------------------------

def eliminarOferta(request, id_Ofertas):
    oferta=Ofertas.objects.get(pk=id_Ofertas)
    oferta.delete()
    ofertas=Ofertas.objects.all()
    return render(request, "postulacionesM.html",{"get_ofertas":ofertas})





































#---------------------------------------------------------------------------

def formulario_actualizacion(request):
    if request.method == 'POST':
        form = Actualizacion(request.POST)
        if form.is_valid():
       
            form.save()
            return redirect('formulario_ofertas')  
    else:
        form = Actualizacion()


    context = {'form': form}
    return render(request, 'candidato/actualizacion.html', context)


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

class OfertaViewSet(viewsets.ModelViewSet):
    queryset=Ofertas.objects.all()
    serializer_class=OfertaSerializer

#-------------------------------------------------------------------------agenda






    
#---------------------------------------------------------------------------
