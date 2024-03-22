from email import message
from django.shortcuts import redirect, render
from django.urls import reverse

from login_usuarios.models import regis_candidato

def validar_usuario(request):
    if request.method == "POST":
        email = request.POST.get("correo")
        password_input = request.POST.get("contraseña_hashed")
        validate = regis_candidato.objects.filter(correo=email).values_list("correo", "contraseña_hashed")
        if len(validate) > 0:
            for i in validate:
                correo = i[0]
                password_db = i[1]
            if email == correo and password_input == password_db:
                return redirect('postulacionesM')
            else:
                return redirect('empresa')
        else:
            return redirect('empresa')
    else:
        return render(request, "error.html", {"message": "Credenciales no válidas."})

def formulario(request):
    if request.method == 'POST':
        user_form = regis_candidato(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return redirect(reverse('formulario') + '?ok')
        else:
            print(user_form.errors)
            return redirect(reverse('formulario') + '?error')
    else:
        user_form = regis_candidato()
    return render(request, 'login/registrarseC.html', {'form': user_form})