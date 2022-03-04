from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView
from .models import Perfil
from .forms import SignUpForm
from django.contrib.auth.views import LoginView

from django.contrib.auth.views import LoginView, LogoutView 

#from .models import Perfil
# Create your views here.
'''
--> Vamos a hacer uso de las vistas basadas en clase, por ahora vamos a usar CreateView y 
    TemplateView para mostrar lo que queremos en el index.
--> Con el CreateView django automaticamente buscara por todo el proyecto la carpeta templates
    un archivo llamado app_form o en este caso perfil_form.html el cual podriamos hacer uso en caso 
    de que necesitemos crear una parte de edicion donde los usuarios puedan actualizar su perfil
'''
class SignUpView(CreateView):
    model = Perfil
    form_class = SignUpForm

    def form_valid(self,form):
        #En esta parte si el formulario es valido guardamos lo que se optiene de el y usamos authenticate
        #para que el usuario inicie sesión luego de haberse registrado y lo redirigimos al index
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username = usuario, password = password)
        login(self.request, usuario)
        return redirect('/')

class BienvenidaView(TemplateView):
    template_name = 'perfiles/bienvenida.html'

'''
Vamos a hacer uso de LoginView, nuevo en Django 1.11, que utiliza el AuthenticationForm que ya 
hace ciertas validaciones por nosotros, por defecto busca un template en registration/login.html 
pero vamos a cambiar eso para colocarlo en el mismo sitio de nuestros otros templates. Otra cosa 
que hace por defecto es que nos redirige al usuario luego de validado el formulario a /accounts/profile/ 
tampoco queremos eso, queremos que vaya al index para que muestre el nombre del usuario registrado.
'''
class SignInView(LoginView):
    template_name = 'perfiles/iniciar_sesion.html'

'''Ahora, para que la vista nos redirija al index después de validado del formulario debemos 
agregar un par de lineas en nuestro settings.py
LOGIN_URL = '/inicia-sesion/'
LOGIN_REDIRECT_URL = '/'
'''
class SignOutView(LogoutView):
    pass