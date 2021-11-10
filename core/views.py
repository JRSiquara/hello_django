from django.shortcuts import render, HttpResponse

# Create your views here.

# def hello(request, nome, idade):
#     return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome, idade))

def soma(request, num1, num2):
     soma_n1n2 = num1 + num2
     return HttpResponse('<h1>Soma {} + {} = {}</h1>'.format(num1, num2, soma_n1n2))

def multiplicacao(request, num1, num2):
     soma_n1n2 = num1 * num2
     return HttpResponse('<h1>Multiplicação {} + {} = {}</h1>'.format(num1, num2, soma_n1n2))