"""Aqui são construídas as tabelas do banco de dados. Isso são os modelos. São representados por classes
Cada classe é uma tabela/modelo.

auto_now-> atualiza a data toda vez que o post é modificado.
auto_now_add-> coloca uma data fixa, no caso a do momento da criação. Não permite modificações.
timezone.now-> funciona como o auto_now_add, mas permite modificar."""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE) # se um usuário é deletado, todos os seus posts também são
    title = models.CharField(max_length=120, null=False, default='No title')
    content = models.TextField(null=False)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title # o que será retornado nas queries
    
    # redirect: redireciona para uma rota específica
    # reverse: retorna a url para a rota como uma string
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk}) # para qual post deve redirecionar 
        
    


    


