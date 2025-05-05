from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .models import Usuario, Disciplina, ReservaAmbiente
from .serializers import UsuarioSerializer, DisciplinaSerializer, ReservaAmbienteSerializer, LoginSerializer
from .permissions import IsGestor, IsProfessor, IsDonoOuGestor
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

class UsuarioListCreate(ListCreateAPIView): #Listar e criar
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsGestor]

class UsuarioRestrieveUpdateDestroy(RetrieveDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    pagination_class = [IsGestor]
    lookup_field = 'pk'

class DisciplinaListCreate(ListCreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsGestor()]
    
class DisciplinaRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    permission_classes = [IsGestor]
    lookup_field = 'pk'

class DisciplinaProfessorList(ListAPIView):
    serializer_class = DisciplinaSerializer
    permission_classes = [IsProfessor]

    def get_queryset(self):
        return Disciplina.objects.filter(professor=self.request.user) #Filtra todas as disciplinas do usuário 'professor' atual
    
class ReservaAmbienteListCreate(ListCreateAPIView):
    queryset = ReservaAmbiente.objects.all()
    serializer_class = ReservaAmbienteSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsGestor()]
    
    def get_queryset(self): #Ver reservar do professor de um ID específico, adiciona um filtro no queryset pai
        queryset = super().get_queryset()
        professor_id = self.request.query_params.get('professor', None)
        if professor_id:
            queryset = queryset.filter(professor_id=professor_id)
        return queryset
    
class ReservaAmbienteRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = ReservaAmbiente.objects.all()
    serializer_class = ReservaAmbienteSerializer
    permission_classes = [IsDonoOuGestor]
    lookup_field = 'pk'

class ReservaAmbienteProfessorList(ListAPIView):
    serializer_class = ReservaAmbienteSerializer
    permission_classes = [IsProfessor]

    def get_queryset(self):
        return ReservaAmbiente.objects.filter(professor=self.request.user) #Filtra só as reservas de um professor específico
    
class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
