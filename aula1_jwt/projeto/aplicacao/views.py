from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import UsuarioDS16
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .serializers import UsuarioSerializer

@api_view(['POST'])
def criar_usuario(request):
    username = request.data.get('username')
    senha = request.data.get('senha')
    idade = request.data.get('idade')
    animais = request.data.get('animais')
    telefone = request.data.get('telefone')
    biografia = request.data.get('biografia')
    endereco = request.data.get('endereco')
    escolaridade = request.data.get('escolaridade')

    if not username or not senha or not idade or not escolaridade:
        return Response({'Erro': 'Campos obrigatórios incompletos'}, status=status.HTTP_400_BAD_REQUEST)
    
    if UsuarioDS16.objects.filter(username=username).exists():
        return Response ({'Erro:' f'Username {username} já existe'}, status=status.HTTP_400_BAD_REQUEST)
    
    usuario = UsuarioDS16.objects.create_user(
        username = username,
        password = senha,
        idade = idade,
        animais = animais,
        telefone = telefone,
        biografia = biografia,
        endereco = endereco,
        escolaridade = escolaridade,
    )
    return Response({'Mensagem': f'Usuario {username} criado com sucesso'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def logar_usuario(request):
    username = request.data.get('username')
    senha = request.data.get('senha')

    usuario = authenticate(username=username, password=senha)

    if usuario:
        refresh = RefreshToken.for_user(usuario)

        return Response({
            'acesso' : str(refresh.access_token),
            'refresh' : str(refresh)
        }, status=status.HTTP_200_OK)
    
    else:
        return Response({'Erro' : 'Usuario ou/e senha incrorreta'}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['GET'])
@permission_classes ([IsAuthenticated])
def read(request):
        usuario = request.user
        return Response({
            'id': usuario.id,
            'idade': usuario.idade,
            'animais': usuario.animais,
            'telefone': usuario.telefone,
            'biografia': usuario.biografia,
            'endereco': usuario.endereco,
            'escolaridade': usuario.escolaridade,
        }, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes ([IsAuthenticated])
def user_put(request, id):
    try:
        atualizar = UsuarioDS16.objects.get(pk=id)
    except UsuarioDS16.DoesNotExist:
        return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = UsuarioSerializer(atualizar, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request, id):
    try:
        usuario = UsuarioDS16.objects.get(pk=id)
    except UsuarioDS16.DoesNotExist:
        return Response({'erro': 'Usuario inexistente'}, status=status.HTTP_404_NOT_FOUND)
    
    username = usuario.username
    usuario.delete()
    return Response({'Mensagem': f'{username} foi apagado'}, status=status.HTTP_200_OK)




    #user adm: admin
    #password: 12345

    #modelo criar:
# {
#    "id": 5,
#    "username": "giovana",
#    "password": "12345",
#    "idade": 17,
#    "animais": 7,
#    "telefone": 124422,
#    "biografia": "uhufwifirwgh3r",
#    "endereco": "griuhriufg",
#    "escolaridade": "medio"
# }

    #modelo criar 2:
#  {
#     "id": 5,
#     "username": "giovana",
#     "senha": "12345",
#     "idade": 17,
#     "animais": 7,
#     "telefone": 124422,
#     "biografia": "uhufwifirwgh3r",
#     "endereco": "griuhriufg",
#     "escolaridade": "medio"
# }

#modelo token de acesso
# {
# "username" : "admin",
# "senha": 12345 #a senha
# }

#modelo token
# "username": "ana",
# "senha": 12345