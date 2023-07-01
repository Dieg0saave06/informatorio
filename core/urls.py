from django.urls import path
from core import views


urlpatterns = [
    path("index/", views.indexView, name = "index"),
    path("publicaciones/", views.publicacionesView, name = "publicaciones"),
    path("mi_perfil/", views.mi_perfilView, name = "mi_perfil"),
    path("ajustes/", views.ajustesView, name = "ajustes"),
    path("cerrar_sesion/", views.cerrar_sesionView, name = "cerrar_sesion"),
]