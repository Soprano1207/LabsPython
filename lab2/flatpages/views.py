from django.http import HttpResponse
from django import template
from django.shortcuts import render


def home(request):
    # Уберите указание типа возвращаемого ответа
    #return HttpResponse('Привет, Мир!')
    
    # Задания ДО создания static_handler
    #return render(request, 'templates/index.html')

    # Задания ПОСЛЕ создания static_handler
    return render(request, 'templates/static_handler.html') 
      

def hello(request):
    # Уберите указание типа возвращаемого ответа
    return HttpResponse('Привет, Мир!')
