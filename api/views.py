from django.shortcuts import render
from django.http import JsonResponse  # simple function to test http responses 

# Create your views here.

def getRoutes(request):  # needs 'request' object passed to it

    return JsonResponse('API works', safe=False)  # safe=Flase allows returning more than just a python dict
