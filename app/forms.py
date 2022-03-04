from msilib.schema import Class
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Perfil
#Creamos el formulario para que el usuario se registre
'''
UserCreationForm -> Trae django por defecto y tendremos los campos del username, contraseña y 
confirmación de esta
User -> Tambien podemos extender ese formulario con los campos que tenemos en modelo user de 
django, asi que tendremos first_name, last_name y email.
'''
#Clase meta
'''
La clase Meta se puede utilizar para definir varias cosas sobre el modelo, como los permisos, 
el nombre de la base de datos, los nombres en singular y plural, abstracción, ordenación, etc. 
Agregar clases Meta a los modelos Django es completamente opcional.
'''

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )
