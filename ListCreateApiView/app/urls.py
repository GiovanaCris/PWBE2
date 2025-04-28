from django.urls import path
from .views import PilotoListCreateAPIView, PilotoRetriveUpdateDestroyAPIView, CarroListCreateAPIView

urlpatterns = [
    path('piloto/', view=PilotoListCreateAPIView.as_view()), #Url de criação e leitura dos pilotos criados
    path('piloto/<int:pk>/', view=PilotoRetriveUpdateDestroyAPIView.as_view()), #Url do CRUD do piloto
    path('carro/', view=CarroListCreateAPIView.as_view()) #Url de leitura e criação do carro
]