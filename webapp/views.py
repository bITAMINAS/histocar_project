from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello, Djangoooooooooo! prueba de commit y si funciona servidor")

def test(request):
    return HttpResponse("Esta es una prueba de la pagina test")

    