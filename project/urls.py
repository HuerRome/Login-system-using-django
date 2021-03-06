"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from app.views import SignInView, SignOutView, SignUpView, BienvenidaView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',BienvenidaView.as_view(), name='bienvenida'),
    path('registrate/',SignUpView.as_view(), name='sign_up'),
    path('inicia-sesion/',SignInView.as_view(), name='sign_up'),
    path('cerrar-sesion/', SignOutView.as_view(), name='sign_out'),
]
#https://platzi.com/contributions/creando-registro-de-usuario-e-inicio-de-sesion-con-django/?gclid=CjwKCAiAyPyQBhB6EiwAFUuakuc5Cz1D749D-jYr7FOysH8mlSrxeqwCd3W0sq4RUNcCOmN6NUp47xoCZPUQAvD_BwE&gclsrc=aw.ds