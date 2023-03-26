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
    # age = request.POST['Age']
    reqData = request.data
    print(type(reqData), reqData)
    
    dataInput = [None]*16
    
    print(dataInput, len(dataInput))
    
    
    dataInput[0] = reqData[0]
    dataInput[1] = reqData[1]

    for i in range(2,len(reqData)):
        dataInput[i] = False
        if('YES' in reqData[i]):
            dataInput[i] = True

    print(dataInput, len(dataInput))
    Age = dataInput[0]
    Gender = dataInput[1]
    Polyuria = dataInput[2]
    Polydipsia = dataInput[3]
    sudden_weight_loss = dataInput[4]
    weakness = dataInput[5]
    Polyphagia = dataInput[6]
    Genital_thrush = dataInput[7]
    visual_blurring = dataInput[8]
    Itching = dataInput[9]
    Irritability = dataInput[10]
    delayed_healing = dataInput[11]
    partial_paresis = dataInput[12]
    muscle_stiffness = dataInput[13]
    Alopecia = dataInput[14]
    Obesity = dataInput[15]
    
    resultResponse = {
        'Age' : Age,
        'Gender' : Gender,
        'Polyuria' : Polyuria,
        'Polydipsia' : Polydipsia,
        'sudden_weight_loss' : sudden_weight_loss,
        'weakness' : weakness,
        'Polyphagia' : Polyphagia,
        'Genital_thrush' : Genital_thrush,
        'visual_blurring' : visual_blurring,
        'Itching' : Itching,
        'Irritability' : Irritability,
        'delayed_healing' : delayed_healing,
        'partial_paresis' : partial_paresis,
        'muscle_stiffness' : muscle_stiffness,
        'Alopecia' : Alopecia,
        'Obesity' : Obesity,
        }
    diabetesPredictionResult = False
    return Response(resultResponse)
    
    