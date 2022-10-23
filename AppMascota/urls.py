from .views import *
from django.urls import path, include
from django.contrib.auth.views import LogoutView



urlpatterns = [

    path('', inicio, name="Home"),

    path("login", inicioSesion, name="Login"),
    path("register", registroUser, name="Registro"),
    path("logout/", LogoutView.as_view(template_name="AppMascota/logout.html"), name="Logout"),
    path("editar/", editarUser, name="EditarUsuario"),
    path("cambiarAvatar/", avatarAgregar, name="Avatar"),
    path("contact/", datosContact, name="Sitio"),
    path("pag/", tarjeta, name="pago"),

    path("about/", about, name="SobreMi"),
    path("oops/", sitioConst, name="NoHaySitio"),
    path("enviado/", mje, name="mjeEnviado"),





    #CRUD Articulo

    path("articulo/list/", ListaArticulo.as_view(), name="ArticuloLeer"),
    path("articulo/<int:pk>", DetalleArticulo.as_view(), name="ArticuloDetalle"),
    path("articulo/crear/", CrearArticulo.as_view(), name="ArticuloCrear"),
    path("articulo/editar/<int:pk>", EditarArticulo.as_view(), name="ArticuloEditar"),
    path("articulo/borrar/<int:pk>", BorrarArticulo.as_view(), name="ArticuloBorrar"),
    path('cambiarPwd/', CambioPassword.as_view(), name='PasswordContra'),
    path('exitoPwd/' , contraConfirmada, name='PasswSuccess'),





    #Adicionales

    #path("about", ListaArticulo.as_view(), name="ArticuloLeer"),
    #path("contacto", ListaArticulo.as_view(), name="ArticuloLeer"),






]

