"""
Criando um profile automaticamente, após um novo usuário ter sido cadastrado
"""
from django.db.models.signals import post_save
from django.contrib.auth.models import User # é o sender, dispara o sinal
from django.dispatch import receiver
from .models import Profile
# sinal disparado depois de um objeto ter sido salvo
# como se fossem triggers sql

@receiver(signal=post_save, sender=User) # quando um usuário é salvo, o decorator recebe o sinal
def create_profile(sender, instance, created, **kwargs):
    """instance e created são argumentos gerados automaticamente pelo receiver
    instance é uma instância do usuário
    created sempre é verdadeiro quando o sinal é recebido pelo decorator"""
    if created:
        # se created é verdadeiro, então crie um perfil
        Profile.objects.create(user=instance)

@receiver(signal=post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()