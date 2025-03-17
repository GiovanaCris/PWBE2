from django.db import models

from django.db import models
class Postagem(models.Model):
 titulo = models.CharField(max_length=200)
 autor = models.TextField()
 ano_publicacao = models.DateTimeField(auto_now_add=True)
 informacoes_adc = models.CharField(max_length=300)
 def __str__(self):
    return self.titulo