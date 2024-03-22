from django.shortcuts import render, redirect
from .forms import HojaVidaForm, HojaVida
from django.shortcuts import render, redirect
from .forms import HojaVidaForm
from rest_framework import viewsets
from .serializer import HojaVidaSerializer



def hoja_vida_view(request):
    hojas_de_vida = HojaVida.objects.all()
    print(hojas_de_vida)
    return render(request, 'candidato/ver_hojas_vida.html', {'hojas_de_vida': hojas_de_vida})


def formulario_agenda(request):
    return render(request,'reclutador/formulario_agendaM.html')


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



def ver(request):
    hojas_de_vida = HojaVida.objects.all()
    print(hojas_de_vida)
    return render(request, 'candidato/ver_hoja_vida.html', {'hojavida': hojas_de_vida})




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


