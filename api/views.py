from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getRoutes(request):
    routes = [
            {
                'Our Routes' : 'Only One Route'
            },
            {
                'Our Routes' : 'Only One Route'
            },
        ]
    return Response(routes)

@api_view(['GET', 'POST'])
def predictDiabetes(request):
    resultResponse = ["Cooking"]
    diabetesPredictionResult = False;
    return Response(resultResponse)
    
    