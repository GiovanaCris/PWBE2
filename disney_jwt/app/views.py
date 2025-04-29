from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UsuarioSerializer, IngressoSerializer, LoginSerializer
from .permissions import IsGestor, IsGestorOuDono
from rest_framework.permissions import IsAuthenticated
from .models import Usuario, Ingresso
from rest_framework_simplejwt.views import TokenObtainPairView

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

class UsuarioListCreateAPIView(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsGestor]

class IngressoRUDAPI(RetrieveUpdateDestroyAPIView):
    queryset = Ingresso.objects.all()
    serializer_class = UsuarioSerializer
    pagination_classes = [IsGestorOuDono]

class IngressoListCreateAPIView(ListCreateAPIView):
    queryset = Ingresso.objects.all()
    serializer_class = IngressoSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()] #AllowAny
        return [IsGestor()]

# class IngressoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Ingresso.objects.all()
#     serializer_class = IngressoSerializer
#     permission_classes = [IsGestorOuDono]
#     lookup_field = 'pk'
#usuario: admin
#senha: 12345