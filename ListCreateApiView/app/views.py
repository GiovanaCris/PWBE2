from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from rest_framework.generics import ListCreateAPIView
from .serializers import PilotoSerializer, CarroSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class PilotoPaginacao(PageNumberPagination): #http://127.0.0.1:8000/piloto/?page=2&page_size1
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10

#CRUD do piloto
class PilotoRetriveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer
    lookup_field = 'pk'

    @swagger_auto_schema(
        operation_description='Pega o piloto do ID fornecido',
        responses={
            200: PilotoSerializer,
            404: 'Not Found',
            400: 'Error'
        }
    )

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    #PUT para atualização das informações do piloto
    @swagger_auto_schema(
        operation_description='Atualiza a informação de um ID fornecido',
        responses={
            200: PilotoSerializer,
            404: 'Not Allowed',
            400: 'Error'
        }
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    #Atualização parcial dos dados do piloto
    @swagger_auto_schema(
        operation_description='Atualiza parcialmente o ID',
        responses={
            200: PilotoSerializer,
            404: 'Not Allowed',
            400: 'Error'
        }
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    #Deletar um piloto
    @swagger_auto_schema(
        operation_description='Deleta um ID',
        responses= {
            200: PilotoSerializer,
            404: 'Not Allowed',
            400: 'Error'
        }
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

#Criação e leitura dos dados do piloto
class PilotoListCreateAPIView(ListCreateAPIView):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer
    pagination_class = PilotoPaginacao

    #Lista todos pilotos cadastrados
    @swagger_auto_schema(
            operation_description='Lista todos os pilotos de Formula 1',
            responses={
                200: PilotoSerializer(many=True),
                404: 'Error'
            },
            manual_parameters= [
                openapi.Parameter(
                    'nome',
                    openapi.IN_QUERY,
                    description='Filtrar pelo nome do piloto',
                    type=openapi.TYPE_STRING
                )
            ]
    )

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    #Cria os campos de preenchimento dos dados piloto que vem do serializer
    @swagger_auto_schema(
            operation_description='Cria um novo piloto',
            request_body=PilotoSerializer,
            responses={
                201: PilotoSerializer,
                400: 'ERROR'
            }

    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
    #Filtra os dados do piloto por id
    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome') #para filtrar o id é o mesmo processo porém no lugar de nome iria passar id
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        return queryset
    
    #Tratação para apenas quem for da DS-16 ficar entre os 5 primeiros colocados na 'equipe'
    def perform_create(self, serializer):
        if serializer.validated_data['equipe'] != 'DS16' and serializer.validated_data['classificacao'] <= 5:
            raise serializers.ValidationError('Somente a DS16 fiicar entre os 5')
        serializer.save()

#Ler e criar o carro
class CarroPaginacao(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 15

#Classe paraa criação e leitura dos carros
class CarroListCreateAPIView(ListCreateAPIView):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
    pagination_class = CarroPaginacao

    #Lista todos carros 
    @swagger_auto_schema(
            operation_description='Lista todos os carros de Formula 1',
            responses={
                200: CarroSerializer(many=True),
                404: 'Error'
            },
            manual_parameters= [
                openapi.Parameter(
                    'marca', #nome
                    openapi.IN_QUERY,
                    description='Filtrar pelo nome do carro',
                    type=openapi.TYPE_STRING
                )
            ]
    )

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    #Cria um novo carro
    @swagger_auto_schema(
            operation_description='Cria um novo Carro',
            request_body=CarroSerializer,
            responses={
                201: CarroSerializer,
                400: 'ERROR'
            }

    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
    #filtra a leitura dos carros por id
    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome') #para filtrar o id é o mesmo processo porém no lugar de nome iria passar id
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        return queryset
    
    #Tratação para se o carro estiver em uma 'velocidade_maxima' que é pego do serilizer que vem do models estiver acima de 100 vai aparecer uma mensagem
    def perform_create(self, serializer):
        if serializer.validated_data['velocidade_maxima'] > 100:
            raise serializers.ValidationError('O carro esta acima da velocidade desejada')
        serializer.save()