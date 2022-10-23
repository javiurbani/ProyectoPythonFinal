from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppMascota.models import Avatar
from django.forms import ModelForm


class FormularioArticulos(forms.Form):

    nombre = forms.CharField()
    animal = forms.CharField()
    categoria = forms.CharField()
    precio = forms.IntegerField()
    fecha = forms.DateField()
    imagen = forms.ImageField()
    


class FormularioReview(forms.Form):

    comentario = forms.CharField()
    usuario = forms.CharField()


class RegistroUser(UserCreationForm):

    email = forms.EmailField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["username", "email", "nombre", "apellido"]


class FormularioUsuario(forms.Form):

    email = forms.EmailField()
    nombre = forms.CharField()
    apellido = forms.CharField()


    class Meta:

        model = User
        fields = ["email", "nombre", "apellido"]


class FormularioAvatar(forms.ModelForm):

    class Meta:

        model = Avatar
        fields = ["imagen"]


#class Formulario

from django.contrib.auth.forms import PasswordChangeForm


class FormularioCambioContra(PasswordChangeForm):

    old_password = forms.CharField(label=("Contraseña actual"), widget=forms.PasswordInput)
    new_password1 = forms.CharField(label=("Nueva contraseña"), widget=forms.PasswordInput)
    new_password2 = forms.CharField(label=("Repetir contraseña"), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')