from django.shortcuts import render
from django.http import JsonResponse  # simple function to test http responses 

# Create your views here.

def getRoutes(request):  # needs 'request' object passed to it

    # example routes / endpoints for the API
    routes = [
        {
            'Endpoint': '/workouts/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a list of workouts'
        },
        {
            'Endpoint': '/workouts/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single workout'
        },
        {
            'Endpoint': '/workouts/create',
            'method': 'POST',
            'body': {'name', 'notes', 'exercises', 'duration', 'date'},
            'description': 'Creates a new workout'
        },
        {
            'Endpoint': '/workouts/id/update',
            'method': 'PUT',
            'body': {'name', 'notes', 'exercises', 'duration', 'date'},
            'description': 'Updates a workout'
        },
        {
            'Endpoint': '/workouts/id/delete',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes a workout'
        },
    ]

    return JsonResponse('API works', safe=False)  # safe=Flase allows returning more than just a python dict
