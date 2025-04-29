from django.db import models
from django.contrib.auth.models import AbstractUser

class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=100)

#Criação da classe usuario
class Usuario(AbstractUser):
    apelido = models.CharField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=100, null=True, blank=True)
    genero = models.CharField(max_length=100, choices=(('M', 'Masculino'), ('F', 'Feminino'), ('N', 'Prefiro não informar')), null=True, blank=True)

    #Escolha da função do colaborador
    escolha_colaborador = (
        ('G', 'Gestor'),
        ('E', 'Estagiario'),
        ('A', 'Aprendiz'),
        ('M', 'Meio oficial'),
    )

    colaborador = models.CharField(max_length=1,
    choices=escolha_colaborador, default='A')

    REQUIRED_FIELDS = ['colaborador']

    Empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True)

class Ingresso(models.Model):
    nome =  models.CharField(max_length=100)
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)