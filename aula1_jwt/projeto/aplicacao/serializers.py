from rest_framework import serializers
from .models import UsuarioDS16 

#Converte modelos Django em JSON
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioDS16
        fields = '__all__'