from django import forms
from .models import Livros

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livros
        fields = '__all__' 

class BuscarLivros(forms.Form):
  nome = forms.CharField(required=False, label = 'Nome do livro: ')
  autor = forms.CharField(required=False, label= 'Nome do autor: ')