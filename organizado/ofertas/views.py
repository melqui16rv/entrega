from django.shortcuts import render, redirect
from django.http import HttpResponse

from hojavida.models import HojaVida
from .forms import OfertaForm, Actualizacion
from .models import Oferta

from rest_framework import viewsets
from .serializer import OfertaSerializer

class OfertaViewSet(viewsets.ModelViewSet):
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer

# ---------------------------------------------------------
def postulacionesM(request):
    data = Oferta.objects.all()
    return render(request, 'reclutador/postulacionesM.html', {'ofertas': data})

def postulacionesC(request):
    data = Oferta.objects.all()
    return render(request, 'candidato/postulacionesC.html', {'ofertas': data})

# ---------------------------------------------------------
def guardar_oferta(request):
    if request.method == 'POST':
        form = OfertaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('postulacionesM')  
    else:
        form = OfertaForm()

    context = {'form': form}
    return render(request, 'reclutador/formulario_ofertas.html', context)

# ---------------------------------------------------------
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

# ---------------------------------------------------------
def editarOfertas(request, id_Ofertas):
    oferta = Oferta.objects.filter(id=id_Ofertas).first()
    form = OfertaForm(instance=oferta)
    return render(request, "reclutador/editarOfertas.html", {"form": form, "oferta": oferta})

# ---------------------------------------------------------
def actualizarOfertas(request, id_Ofertas):
    oferta = Oferta.objects.get(pk=id_Ofertas)
    form = OfertaForm(request.POST, instance=oferta)
    if form.is_valid():
        form.save()
        return redirect('postulacionesM')  # Redirigir a la página de postulaciones después de actualizar
    return render(request, "reclutador/postulacionesM.html")  # Asegúrate de devolver una respuesta si el formulario no es válido

# ---------------------------------------------------------
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

# ---------------------------------------------------------
def eliminarOferta(request, id_Ofertas):
    oferta = Oferta.objects.get(pk=id_Ofertas)
    oferta.delete()
    return redirect('postulacionesM')  # Redirigir a la página de postulaciones después de eliminar

# ---------------------------------------------------------



def postularse_oferta(request, oferta_id):
    oferta = Oferta.objects.get(pk=oferta_id)

    hoja_vida = HojaVida.objects.get(usuario=request.user)  

    if hoja_vida.educacion == oferta.educacion and \
       hoja_vida.experiencia == oferta.experiencia and \
       hoja_vida.profesion == oferta.profecion:
        
        return redirect('postulacion_exitosa')  
    else:
        return redirect('postulacion_fallida')  
