from django.db import models

class Eventos(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    data_hora = models.DateTimeField()
    local = models.TextField(blank=True, null=True)
    escolha_categoria = (
        ('MUSICA', 'Musica'),
        ('PALESTRA', 'Palestra'),
        ('WORKSHOP', 'Workshop')
    )
    categoria = models.TextField(blank=True, null=True, choices=escolha_categoria)

    def __str__(self):
        return self.nome