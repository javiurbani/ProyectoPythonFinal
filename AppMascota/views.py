from multiprocessing import AuthenticationError
from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

#Home/Inicio

def inicio(request):

    return render(request, 'inicio.html')

#Login y Logout

def inicioSesion(request):

    if request.method =="POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contra)

            if user:

                login(request, user)
                return render(request, "AppMascota/inicio.html", {"mensaje":f"Bienvenido {user}"})
        
        else:

            return render(request, "AppMascota/login.html", {"mensaje2":f"Los datos son incorrectos."})

    else:

        form = AuthenticationForm()
    
    return render(request, "AppMascota/login.html", {"formulario":form})



def registroUser(request):

    if request.method == "POST":

        form = RegistroUser(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()
            
            return render(request, "AppMascota/inicio.html", {"mensaje2": f"¡Usuario creado con éxito!"})
    
    else: 
        
        form = RegistroUser()

    return render(request, "AppMascota/registro.html", {"formulario":form})


@login_required
def editarUser(request):

    usuario = request.user

    if request.method == "POST":

        form = FormularioUsuario(request.POST)

        if form.is_valid():

            info = form.cleaned_data
            usuario.email = info["email"]
            usuario.first_name = info["nombre"]
            usuario.last_name = info["apellido"]
            usuario.save()

            return render(request, "inicio.html")
    
    else:

        form = FormularioUsuario(initial={
            "email":usuario.email,
            "nombre":usuario.first_name,
            "apellido":usuario.last_name,
            })

    return render(request, "editarPerfil.html", {"form":form, "usuario":usuario})


@login_required
def avatarAgregar(request):

    if request.method =="POST":

        form = FormularioAvatar(request.POST, request.FILES)

        if form.is_valid():

            usuarioActual = User.objects.get(username=request.user)

            avatar = Avatar(usuario=usuarioActual, imagen=form.cleaned_data["imagen"])

            avatar.save()

            return render(request, "inicio.html")
    
    else:

        form = FormularioAvatar()
    
    return render(request, "agregarAvatar.html", {"formulario":form})

class CambioPassword(PasswordChangeView):

    form_class = FormularioCambioContra
    template_name = 'AppMascota/cambioContra.html'
    success_url = reverse_lazy('PasswSuccess')


def contraConfirmada(request):

    return render(request, 'AppMascota/contraExitosa.html')


#Articulos CRUD


class ListaArticulo(ListView):

    model = Articulo
    template_name = "articulo_list.html"


class DetalleArticulo(LoginRequiredMixin, DetailView):

    model = Articulo
    login_url = "login.html"
    template_name = "articulo_detail.html"


class CrearArticulo(LoginRequiredMixin, CreateView):

    model = Articulo
    success_url = "/AppMascota/articulo/list/"
    login_url = "login.html"
    template_name = "articulo_form.html"
    fields = "__all__"
    

class EditarArticulo(LoginRequiredMixin, UpdateView):

    model= Articulo
    success_url = "/AppMascota/articulo/list/" 
    login_url = "login.html"
    fields = "__all__"


class BorrarArticulo(LoginRequiredMixin, DeleteView):

    model= Articulo
    success_url = "/AppMascota/articulo/list"
    login_url = "login.html"
    template_name = "articulo_confirm_delete.html"



def about(request):

    return render(request, "about.html")


def sitioConst(request):

    return render(request, "enConstruccion.html")



def datosContact(request):

    return render(request, "contactod.html")


def tarjeta(request):

    return render(request, "pago.html")

def mje(request):

    return render(request, "mensaje.html")

