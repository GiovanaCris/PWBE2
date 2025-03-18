from rest_framework import serializers
from .models import Carro

#Conversão do modelo para JSON
class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = '__all__'