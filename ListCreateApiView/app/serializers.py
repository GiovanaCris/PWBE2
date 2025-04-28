from rest_framework import serializers
from .models import *

#Converte o piloto para Json com a classe 'PilotoSerializer'
class PilotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piloto
        fields = '__all__'

#Converte o carro para Json com a classe 'CarroSerializer'
class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = '__all__'