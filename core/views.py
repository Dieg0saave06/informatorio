from django.shortcuts import render

# Create your views here.


def indexView(request):
    return render(request, "index.html", {})

def publicacionesView(request):
    return render(request, "publicaciones.html", {})

def mi_perfilView(request):
    return render(request, "mi_perfil.html", {})

def ajustesView(request):
    return render(request, "ajustes.html", {})

def cerrar_sesionView(request):
    return render(request, "cerrar_sesion.html", {})
    