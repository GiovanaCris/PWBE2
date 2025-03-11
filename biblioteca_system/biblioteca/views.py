from django.shortcuts import render, redirect, get_object_or_404
from .models import Livros
from .forms import LivroForm
from .forms import BuscarLivros

def livro_read(request):
    livros = Livros.objects.all()
    return render(request, 'lista_livros.html', {'livros': livros})

def livro_create(request):
    if request.method == 'POST':
        listform = LivroForm(request.POST)
        if listform.is_valid():
            listform.save()
            return redirect('livro_read')
    else:
        listform = LivroForm()
    return render(request, 'ver_livroscad.html', {'livros': listform})

def livro_update(request, pk):
    livro = get_object_or_404(Livros, pk=pk)
    if request.method == 'POST':
        listform = LivroForm(request.POST, instance=livro)
        if listform.is_valid():
            listform.save()
            return redirect('livro_read')
    else:
        listform = LivroForm(instance=livro)
    return render(request, 'ver_livroscad.html', {'livros': listform})

def livro_delete(request, pk):
    livro = get_object_or_404(Livros, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('livro_read')
    return render(request, 'deletar_livro.html', {'livros': livro})

def pesquisar_livro(request):
    livros = Livros.objects.all()

    titulo = request.GET.get('titulo', '')
    autor = request.GET.get('autor', '')

    if titulo:
        livros = livros.filter(titulo__icontains=titulo)
    if autor:
        livros = livros.filter(autor__icontains=autor)
 
    return render(request, 'lista_livros.html', {
        'titulo': titulo,
        'autor': autor,
    })