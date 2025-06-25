from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import sys

def home(request):
    response = HttpResponse('Hello woo')
    return response

def info(request):
    r = HttpResponse(sys.version)
    return r

def data(request):
    d = {
        '67000000' : {
            'first_name' : 'Anna',
            'last_name' : 'bell'
        },
        '67000001' : {
            'first_name' : 'benedict',
            'last_name' : 'bentenison'
        }
    }
    return JsonResponse(d)

def pdf(request):
    buffer = io.ByteIO()
    p = canvas.Canvas