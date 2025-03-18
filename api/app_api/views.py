from django.shortcuts import render
from .models import Carro
from .serializers import CarroSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

#Lista todos os carros criados utilizando o object.all para pegar todos os objetos da classe
@api_view(['GET'])
def read_carros(request):
    carros = Carro.objects.all()
    serializer = CarroSerializer(carros, many=True)
    return Response(serializer.data)

#Busca um carro em específico através do get.(pk=pk) que é o ID do carro e caso a id pesquisada não exista irá aparecer "erro: carro inexistente"
@api_view(['GET'])
def pegar_carro(request, pk):
    try:
        carro = Carro.objects.get(pk=pk)
    except Carro.DoesNotExist:
        return Response({'erro': 'Carro inexistente'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = CarroSerializer(carro)
    return Response(serializer.data)

#Cria o carro e armazena os dados na classe create_carro
@api_view(['POST'])
def create_carro(request):
    if request.method == 'POST':
        serializer = CarroSerializer(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#Atualiza as informações do carro através da sua ID e caso a ID não exista irá aparecer "erro: Carro enexistente"
@api_view(['PUT'])
def update_carro(request, pk):
    try:
        carro = Carro.objects.get(pk=pk)
    except Carro.DoesNotExist:
        return Response({'erro': 'Carro inexistente'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = CarroSerializer(carro, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Deleta um carro em específico através de sua ID
@api_view(['DELETE'])
def delete_carro(request, pk):
    try:
        carro = Carro.objects.get(pk=pk)
    except Carro.DoesNotExist:
        return Response({'erro': 'Carro inexistente'}, status=status.HTTP_404_NOT_FOUND)
    
    carro.delete()
    return Response({'Mensagem':f'O  seu {carro.nome} foi apagado'}, status=status.HTTP_200_OK)
