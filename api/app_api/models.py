from django.db import models

class Carro(models.Model):
    #Na classe Carro foi passada todas as carxterística do nosso carro, determinando tamanho máximo e escolha de combustível.
    nome = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    qntRodas = models.PositiveIntegerField()
    ano = models.PositiveIntegerField()
    cor = models.CharField(max_length=255)
    escolha_combustivel = (
        ('GASOLINA', 'Gasolina'),
        ('ETANOL', 'Etanol'),
        ('GNV', 'GNV'),
        ('ELETRICO', 'Eletrico'),
        ('ALCOOL', 'Alcool'),
        ('DIESEL', 'Diesel'),
        ('FB', "FeedBack"),
        )
    combustivel = models.CharField(max_length=9, choices=escolha_combustivel)

    def __str__(self):
        return self.nome