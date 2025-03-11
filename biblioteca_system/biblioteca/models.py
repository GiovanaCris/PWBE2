from django.db import models

from django.db import models
class Livros(models.Model):
 titulo = models.CharField(max_length=200)
 autor = models.CharField(max_length=300)
 ano_publi = models.DateTimeField(auto_now_add=True)
 informacoes_adc = models.TextField(max_length=300)
 
 def __str__(self):
    return self.titulo

