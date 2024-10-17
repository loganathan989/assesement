from django.http import JsonResponse
import datetime
from .models import *
# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import *

from django.shortcuts import render
from django.http import HttpResponse


@api_view(['GET', 'POST'])
def Account_list(request,):
    if request.method == 'GET':
        data = Account.objects.all()
        serializer = AccountSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer =AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT', 'DELETE'])
def Account_detail(request, pk):
    try:
        student =  Account.objects.get(GatepassId=pk)
    except  Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer =AccountSerializer(student, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def getAccountById(request,id):            
        productList =Account.objects.filter(id=id)  
        productListSerializer =AccountSerializer(productList, many=True)
        if(len(productListSerializer.data)>0) :

           return JsonResponse(productListSerializer.data[0],safe=False)
        else :
           return JsonResponse(productListSerializer.data,safe=False)
        

