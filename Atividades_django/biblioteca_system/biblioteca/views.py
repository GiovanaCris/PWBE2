from django.shortcuts import render, redirect, get_object_or_404
from .models import Livros
from .forms import LivroForm

def livro_read(request):
    livros = Livros.objects.all()
    return render(request, 'ver_livroscad.html', {'Livros': livros})

def livro_create(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livro_read')
    else:
        form = LivroForm()
    return render(request, 'livro_form.html', {'Livro': LivroForm})

def livro_update(request, pk):
    livro = get_object_or_404(livro, pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('livro_read')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'ver_livroscad.html', {'Livros': livro})

def livro_delete(request, pk):
    item = get_object_or_404(Livros, pk=pk)
    if request.method == 'POST':
        livro_delete()
        return redirect('livro_read')
    return render(request, 'confirmar_delete.html', {'Livros': Livros})
