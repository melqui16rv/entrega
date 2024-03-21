from django.shortcuts import redirect, render

from oferta.forms import Actualizacion, OfertaForm
from oferta.models import Oferta
from oferta.serializer import OfertaSerializer
from rest_framework import viewsets


# Create your views here.

#---------------------------------------------------------
def postulacionesM(request):
    data = Oferta.objects.all()
    return render(request, 'reclutador/postulacionesM.html', {'oferta': data})

def postulacionesC(request):
    data = Oferta.objects.all()
    return render(request, 'candidato/postulacionesC.html', {'oferta': data})


#---------------------------------------------------------
def guardar_oferta(request):
    if request.method == 'POST':
        form = OfertaForm(request.POST)
        if form.is_valid():
            
            form.save()
            return redirect('reclutador/formulario_oferta')
    else:
        form = OfertaForm()

    context = {'form': form}
    return render(request, 'reclutador/formulario_ofertas.html', context)


#---------------------------------------------------------
def formulario_oferta(request):
    if request.method == 'POST':
        form = OfertaForm(request.POST)
        if form.is_valid():
       
            form.save()
            return redirect('formulario_oferta')  
    else:
        form = OfertaForm()


    context = {'form': form}
    return render(request, 'reclutador/formulario_ofertas.html', context)



#---------------------------------------------------------
def editarOferta(request,id_Oferta):
    oferta=Oferta.objects.filter(id=id_Oferta).first()
    form=OfertaForm(instance=oferta)
    return render(request, "reclutador/editarOferta.html",{"form":form,"oferta":oferta})

#---------------------------------------------------------
def actualizarOferta(request,id_Oferta):
    oferta=Oferta.objects.get(pk=id_Oferta)
    form=OfertaForm(request.POST,instance=oferta)
    if form.is_valid():
       form.save()
       get_oferta=Oferta.objects.all()
       {"get_oferta":get_oferta}
    return render(request,"reclutador/postulacionesM.html")
    # return print("okey"),{"get_oferta":get_oferta}




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







    
    
    
    
    
    
    
    
    

#------------------------------------------------------------------------

def eliminarOferta(request, id_Oferta):
    oferta=Oferta.objects.get(pk=id_Oferta)
    oferta.delete()
    oferta=Oferta.objects.all()
    return render(request, "postulacionesM.html",{"get_oferta":Oferta})


class OfertaViewSet(viewsets.ModelViewSet):
    queryset=Oferta.objects.all()
    serializer_class=OfertaSerializer


