from rest_framework import serializers
from .models import Eventos

#Conversão do modelo para JSON
class EventosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eventos
        fields = '__all__'