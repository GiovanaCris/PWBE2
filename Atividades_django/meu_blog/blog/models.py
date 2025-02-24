from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=300)
    conteudo = models.TextField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

# Create your models here.
