from django.shortcuts import render, redirect
from .forms import HojaVidaForm, HojaVida
from django.shortcuts import render, redirect
from .forms import HojaVidaForm
from rest_framework import viewsets
from .serializer import HojaVidaSerializer


def formulario_agenda(request):
    return render(request,'reclutador/formulario_agenda.html')


def hoja_vida_form(request):
    if request.method == 'POST':
        form = HojaVidaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('hoja_vida_form_success')
    else:
        form = HojaVidaForm()

    return render(request, 'hoja_vida_form.html', {'form': form})
#---------------------------------------------------------------------#---------------------------------------------------------------------




def hoja_vida_view(request):
    return render(request, 'candidato/hoja_vida.html')



def llenarHojaVida(request):
    if request.method == 'POST':
        form = HojaVidaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('llenarHojaVida')
    else:
        form = HojaVidaForm()

    return render(request, 'candidato/llenarHojaVida.html', {'form': form})

class HojaVidaViewSet(viewsets.ModelViewSet):
    queryset=HojaVida.objects.all()
    serializer_class=HojaVidaSerializer

    