from django.db import models
from django.contrib.auth.models import AbstractUser

#Modelo da tabela do banco de dados e definição dos campos
class UsuarioDS16(AbstractUser):
    idade = models.PositiveIntegerField()
    animais = models.PositiveIntegerField()
    telefone = models.CharField(max_length=255)
    biografia = models.TextField()
    endereco = models.CharField(max_length=255, null=True, blank=True)
    escolaridade = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self): 
        return self.username