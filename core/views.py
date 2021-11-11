from django.shortcuts import render, HttpResponse

class Error(Exception):  # Classe de exceção personalizada. É obrigação ter sempre essas
    pass                 # duas classes "Error e InputError".

class InputError(Error):  # Por convenção toda classe deve terminar com "Error".
    def __init__(self, message): # Criando um construtor (Ver na aula de classes).
        self.message = message

while True:
     try:
          print('Qual URLs deseja (H)ello, (S)oma, (M)ultiplicação, (D)ivisão, s(U)btração')
          print('Digite a letra entre correspondente () a sua opção ?')
          lst_opcao = {'H', 'S', 'M', 'D', 'U'}
          lopcao = set(str.upper(input()))
          if not lopcao.issubset(lst_opcao):
               raise InputError('Opção inválida!!!')
          else:
               opcao = "".join(list(lopcao))
               break
     except InputError as ex:
          print(ex)

# Create your views here.
if opcao == 'H':
     def hello(request, nome, idade):
          return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome, idade))
elif opcao == 'S':
     def soma(request, num1, num2):
          soma_n1n2 = num1 + num2
          return HttpResponse('<h1>Soma {} + {} = {}</h1>'.format(num1, num2, soma_n1n2))
elif opcao == 'M':
     def multi(request, num1, num2):
          mult_n1n2 = num1 * num2
          return HttpResponse('<h1>Multiplicação {} X {} = {}</h1>'.format(num1, num2, mult_n1n2))
elif opcao == 'D':
     def divisao(request, num1, num2):
          div_n1n2 = int(num1 / num2)
          return HttpResponse('<h1>Divisao {} / {} = {}</h1>'.format(num1, num2, div_n1n2))
elif opcao == 'U':
     def subtracao(request, num1, num2):
          sub_n1n2 = num1 - num2
          return HttpResponse('<h1>Subtração {} - {} = {}</h1>'.format(num1, num2, sub_n1n2))
