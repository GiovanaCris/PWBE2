from rest_framework import serializers
from .models import UsuarioDS16 

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioDS16
        fields = '__all__'