from django.urls import path
from . import views

#Caminhos (Urls) do  projeto
urlpatterns = [
    path('criar/', view=views.criar_usuario, name='criar_usuario'), #URL para criar usuario
    path('logar/', view=views.logar_usuario, name='logar_usuario'), #URL para logar o usuário
    path('read/', view=views.read, name='read'), #RUL para ler as informações dos usuários
    path('atualizar/<int:id>/', view=views.user_put, name='user_put'), #URL para atualizar os dados de um usuário
    path('deletar/<int:id>/', view=views.delete_user, name='delete_user'), #URL para deletar um usuário
]