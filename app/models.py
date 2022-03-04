from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
''' 
creamos un modelo llamado Perfil y extendemos del modelo usuario que trae Django el cual ya 
contiene Username, Nombre, Apellido, Email, Contraseña
'''
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, blank=True)
    web = models.URLField(blank=True)

    def __str__(self):
        return self.usuario.username

'''
En las últimas dos funciones hacemos uso de los signals específicamente del post_save que lo 
que hace es crear el perfil después que un usuario es registrado, con esto aseguramos que el 
usuario tenga perfil.
'''
        
@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_usuario_perfil(sender, instance, **kwargs):
    instance.perfil.save()