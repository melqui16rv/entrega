from django.http import HttpResponse
from django.shortcuts import render, redirect
# from flask import request
from rest_framework import viewsets
from .models import Agenda
from .serealizers import AgendaSerializer
from .forms import AgendaForm

def formulario_agendaM(request):
    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'reclutador/formulario_agendaM.html',)
    else:
        form = AgendaForm()

    return render(request, 'reclutador/formulario_agendaM.html', {'form': form})

def formulario_agendaC(request):
    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'candidato/formulario_agendaC.html',)
    else:
        form = AgendaForm()

    return render(request, 'candidato/formulario_agendaC.html', {'form': form})


def agenda_form(request):
    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agenda_form_success')
    else:
        form = AgendaForm()

    return render(request, 'candidato/formulario_agendaM.html', {'form': form})

# def agenda_formC(request):
#     if request.method == 'POST':
#         form = AgendaForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('agenda_formC_success')
#     else:
#         form = AgendaForm()

#     return render(request, 'agenda_formC.html', {'form': form})


# def agenda_viewM(request):
#     agendas = Agenda.objects.all()
#     return render(request, 'reclutador/agendaM.html', {'agendas': agendas})

def agenda_view(request):
    agendas = Agenda.objects.all()
    return render(request, 'candidato/agendaC.html', {'agendas': agendas})

class AgendaViewSetM(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer

    def formulario_agenda(request):
        if request.method == 'POST':
            form = AgendaForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'reclutador/formulario_agendaM.html',)
        else:
            form = AgendaForm()

            return render(request, 'reclutador/formulario_agendaM.html',)

class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer

    def formulario_agendaC(request):
        if request.method == 'POST':
            form = AgendaForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'candidato/formulario_agendaC.html',)
        else:
            form = AgendaForm()

            return render(request, 'candidato/formulario_agendaC.html',)



def llenar_formulario_agendaM(request):
    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'reclutador/formulario_agendaM.html',)
    else:
        form = AgendaForm()

def llenar_formulario_agendaC(request):
    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'candidato/formulario_agendaC.html',)
 # Reemplaza 'ruta_exitosa' con la URL a la que quieres redirigir después de guardar el formulario
    else:
        form = AgendaForm()

    return render(request, 'candidato/formulario_agendaC.html',)

def agendaC(request):
    agendas = Agenda.objects.all()
    return render(request, 'candidato/agendaC.html', {'agendas': agendas})

def agendaM(request):
    agendas = Agenda.objects.all()
    return render(request, 'reclutador/agendaM.html', {'agendas': agendas})
#---------------------------------------------------------------------- botones de agenda
def editar_agendaM(request, agenda_id):
    try:
        agenda = Agenda.objects.get(id=agenda_id)
    except Agenda.DoesNotExist:
        # Manejar el caso donde la Agenda no existe
        return HttpResponse("La Agenda no existe.")

    if request.method == 'POST':
        form = AgendaForm(request.POST, instance=agenda)
        if form.is_valid():
            form.save()
            return redirect('agenda')

    return render(request, 'reclutador/formulario_agendaM.html', {"form": form, "agenda": agenda})

def eliminar_agendaM(request, agenda_id):
    try:
        agenda = Agenda.objects.get(id=agenda_id)
        agenda.delete()
        return redirect('agenda')  # Redirige a la página de la agenda después de eliminar
    except Agenda.DoesNotExist:
        return HttpResponse("La agenda que intentas eliminar no existe.")
    
    
    
    
    
def editar_agendaC(request, agenda_id):
    try:
        agenda = Agenda.objects.get(id=agenda_id)
    except Agenda.DoesNotExist:
        # Manejar el caso donde la Agenda no existe
        return HttpResponse("La Agenda no existe.")

    if request.method == 'POST':
        form = AgendaForm(request.POST, instance=agenda)
        if form.is_valid():
            form.save()
            return redirect('agenda')

    return render(request, 'candidato/formulario_agendaC.html', {"form": form, "agenda": agenda})

def eliminar_agendaC(request, agenda_id):
    try:
        agenda = Agenda.objects.get(id=agenda_id)
        agenda.delete()
        return redirect('agenda')  # Redirige a la página de la agenda después de eliminar
    except Agenda.DoesNotExist:
        return HttpResponse("La agenda que intentas eliminar no existe.")