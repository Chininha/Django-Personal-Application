"""O modelo de usuários padrão do Django não possui um campo para fotos de perfil
Será preciso estender esse modelo e criar um novo em cima, com uma relação de 1 para 1, ou seja,
um usuário só poder um perfil, e um perfil só pode ser de um usuário.
"""
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
     user = models.OneToOneField(to=User, on_delete=models.CASCADE) # campo que tem relacionamento de um para um com a tabela de usuário
     image = models.ImageField(default='default.jpg', upload_to='profile_pics')

     def __str__(self):
          return f'{self.user.username}'
     
     def save(self): # redefindo o tamanho da imagem e simulando função de save
          super().save()

          img = Image.open(self.image.path)
          
          if img.height > 300 or img.width > 300:
               output_size = (300, 300)
               img.thumbnail(output_size)
               img.save(self.img.path) 
