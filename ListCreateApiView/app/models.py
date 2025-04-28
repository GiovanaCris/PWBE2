from django.db import models

#Cria o modelo Piloto no banco de dados
class Piloto(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.PositiveIntegerField()
    classificacao = models.PositiveIntegerField()
    equipe = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nome} esta na {self.classificacao} posição'

#Cria o modelo Carro no banco de dados
class Carro(models.Model):
    nome = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    velocidade_maxima = models.PositiveIntegerField()
    escolhas_cores = {
        ('VERMELHO', 'Vermelho'),
        ('ROSA', 'Rosa'),
        ('BRANCO', 'Branco'),
        ('PRETO', 'Preto'),
        ('CINZA', 'Cinza'),
    }
    cor = models.CharField(max_length=50, choices=escolhas_cores)
    piloto = models.ForeignKey(Piloto, on_delete=models.CASCADE)