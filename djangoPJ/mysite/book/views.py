from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return HttpResponse("ยินดีต้อนรับสู่ Book App!")
