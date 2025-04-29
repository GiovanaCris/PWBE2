from rest_framework import serializers
from .models import Usuario, Empresa, Ingresso
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

#Serializa todos os dados do modelo Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

#Serializa todos os campos do modelo Empresa
class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

#Serializa o TokenObtainPairSerializer para Json com a classe LoginSerializer
class LoginSerializer (TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs) #Vai puxar a validação do TokenObtainPairSerializer
        data['usuario'] = {
            'id': self.user.id,
            'username': self.user.username,
        }
        return data
    
class IngressoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingresso
        fields = '__all__'