from django.shortcuts import render
from .models import Post

def lista_postagens(request):
 postagens = Post.objects.all().order_by('-status')
 return render(request, 'lista_postagens.html', {'postagens': postagens})

# Create your views here.