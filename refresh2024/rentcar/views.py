from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rentcar.models import Car
import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CarSerializer



@api_view(['GET'])
def getAPI(request):
    return Response("nice")


@api_view(['GET'])
def Carlist(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars,many=True)
    return Response(serializer.data)


# Create your views here.
a = { 
    "name":"John", 
    "age":30, 
    "car":"Volvo" 
}

b= [1,3]

def showcar(request):
	return HttpResponse('This is the list of cars');

def jsotest(request):
	return JsonResponse(a)

#def list(request):
#    data = Car.objects.
#    #json_data = json.dumps(list(data))
#    return JsonResponse(list(data))