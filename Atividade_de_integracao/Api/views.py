from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status
from . import serializers
from .models import produto
from . import models

# Create your views here.
@api_view(['GET'])
def getAllProduto(request):
        if request.method == 'GET':   
            produtos = models.produto.objects.all()
            serializer = serializers.ProdutoSerializer(produtos,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
@api_view(['POST'])
def postProduto(request):
        serializer = serializers.ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# @api_view(['GET'])
# def getProduto(request):
#         ...
# @api_view(['PUT'])
# def putProduto(request):
#         ...
# @api_view(['DELETE'])
# def deleteProduto(request):
#         ...

@api_view(['GET', 'PUT', 'DELETE'])
def produto_detail(request, pk):
    try:
        produto = produto.objects.get(pk=pk)
    except produto.DoesNotExist:
        return Response({'error': 'Produto não encontrado'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.ProdutoSerializer(produto)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializer.ProdutoSerializer(produto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)