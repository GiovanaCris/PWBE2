from django.shortcuts import render
from .models import Eventos
from .serializers import EventosSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from datetime import datetime, timedelta

#Lista os eventos disponíveis
@api_view(['GET'])
def lista_eventos(request):
    eventos = Eventos.objects.all()
    categorias = request.query_params.get('categoria')
    datas = request.query_params.get('data_hora')
    quantidade = request.query_params.get('quantidades')
    ordenacao = request.query_params.get('ordenacao')

    if categorias: #filtro categorias
        eventos = eventos.filter(categoria__icontains = categorias)
    elif datas: #filtro datas
        eventos = eventos.filter(data_hora__icontains = datas)
    elif quantidade: #filtro quantidades
        try: 
            quantidade = int(quantidade)
            eventos = eventos [:quantidade] #Limita o controle de quantidade dependendo da quantidade que o usuário digita
        except ValueError:
            return Response ("Error: Digite um valor válido", status=400) #Retorna um erro caso a quantidade digitada seja negativa ou float
    if ordenacao:
        eventos = eventos.order_by('data_hora').values()
        
    serializer = EventosSerializer(eventos, many=True)
    return Response(serializer.data)

#Pegar um evento em específico
@api_view(['GET'])
def id_eventos(request, pk):
    try: 
        evento = Eventos.objects.get(pk=pk) #pega a id específica conforme o que o usuário irá digitar
    except Eventos.DoesNotExist:
        return Response({'erro': 'Evento não agendado'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = EventosSerializer(evento)
    return Response(serializer.data)

@api_view(['GET'])
def proximos_eventos(request):
    dataatual = datetime.now() #data atual
    datafutura = dataatual + timedelta(days=7) #data em um intervalo de 7 dias

    try:
        evento = Eventos.objects.all()
    except Eventos.DoesNotExist: #Caso de erro se não tiver eventos no intervalo de 7 dias
        return Response ({'error: Evento não cadastrado!'})
    
    proximos_eventos = Eventos.objects.filter(data_hora__gte=dataatual, data_hora__lte=datafutura)

    serializer = EventosSerializer(proximos_eventos, many=True)
    return Response(serializer.data)

#Cria um novo evento
@api_view(['POST'])
def criar_evento(request):
    if request.method == 'POST':
        serializer = EventosSerializer(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#Edita as informações de um evento
@api_view(['PUT'])
def editar_evento(request, pk):
    try:
        evento = Eventos.objects.get(pk=pk)
    except Eventos.DoesNotExist:
        return Response({'erro': 'Evento não agendado'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = EventosSerializer(evento, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Deletar um evento
@api_view(['DELETE'])
def deletar_evento(request, pk):
    try:
        evento = Eventos.objects.get(pk=pk)
    except Eventos.DoesNotExist:
         return Response({'erro': 'Evento inexistente'}, status=status.HTTP_404_NOT_FOUND)
    
    evento.delete()
    return Response({'Mensagem':f'O evento {evento.nome} foi apagado'}, status=status.HTTP_200_OK)
