from django.urls import path
from . import views

#Caminho das URLs
urlpatterns =[
    path('eventos/', views.lista_eventos),
    path('eventos/buscar/<int:pk>', views.id_eventos),
    path('eventos/criar', views.criar_evento),
    path('eventos/atualizar/<int:pk>', views.editar_evento),
    path('eventos/deletar/<int:pk>', views.deletar_evento),
    path('eventos/proximos/', views.proximos_eventos),
]
