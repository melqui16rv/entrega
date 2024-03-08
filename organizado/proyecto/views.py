from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'inicio1.html')



# def login(request):
#     return render(request,'reclutador/index1.html')

# def agenda(request):
#     return render(request,'reclutador/agenda.html')

# def hoja_vida(request):
#     return render(request,'candidato/hoja_vida.html')

# def notificaciones(request):
#     return render(request,'reclutador/notificaciones.html')

# def postulaciones(request):
#     return render(request,'candidato/postulaciones.html')

# def navegador(request):
#     return render(request,'pag/navegador.html')

# def contacta(request):
#     return render(request,'pag/contacta.html')

# def formulario_ofertas(request):
#     return render(request,'reclutador/formulario_ofertas.html')

# def nosotros(request):
#     return render(request,'pag/nosotros.html')

# def usuarios(request):
#     return render(request,'usuariolist.html')

# def usuariolist(request):
#     get_usuarios=Usuario.objects.all()
#     data={
#         'get_usuarios':get_usuarios
#     }
#     return render(request,'usuariolist.html',data)