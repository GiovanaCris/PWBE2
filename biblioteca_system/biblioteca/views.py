from django.shortcuts import render, redirect, get_object_or_404
from .models import Livros
from .forms import LivroForm

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
    obj = request.GET.get('obj')
    livros = []

    if obj: 
        livros = Livros.objects.filter(titulo__icontains=obj)

    else: 
        livros = Livros.objects.all()

    return render(request, 'lista_livros.html', {'livros': livros, 'pesquisado': bool(obj)})



    # obj = request.GET.get('obj') 
    # livros = [] 

    # if obj: 
    #     livros = Livros.objects.filter(titulo__icontains=obj) 

    # if not obj:
    #     livros = Livros.objects.all()

    # return render(request, 'lista_livros.html', {'livros': livros, 'pesquisado': bool(obj)})

    # obj = request.GET.get('obj')
    # livros = []

    # if obj:
    #     livros = Livros.objects.filter(titulo__icontains=obj)

    # return render(request, 'lista_livros.html', {'livros': livros, 'pesquisado': bool(obj)})



    # obj = request.GET.get('obj')
    # livros = []

    # if obj:
    #     livros = Livros.objects.filter(titulo__icontains=obj)

    # else:
    #     livros = Livros.objects.all()

    # return render(request, 'lista_livros.html', {'livros': livros})



    # print(obj)
    # if obj:
    #     livro_read = Livros.objects.filter(name__icontains=obj)
    
    # else:
    #     livro_read = Livros.objects.all()

    # page_number = request.GET.get('page')

    # return render(request, 'lista_livros.html')
