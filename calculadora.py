#!/bin/bash


#calculadora

def menu():
  print("1. Soma")
  print("2. Subtração")
  print("3. Multiplicação")
  print("4. Divisão")
  print("5. Sair")

def soma(valor1, valor2):
  return valor1 + valor2


def subtracao(valor1,valor2):
  return valor1 - valor2

def divisao(valor1, valor2):
    if valor2 != 0:
        return valor1 / valor2
    else:
        return "Erro, divisão por zero"

def multiplicacao (valor1,valor2):
  return valor1 * valor2


while True:
    menu()
    opcoes = input("Selecione o Numero da operação:")

    if opcoes == "5":
      print('saindo')
      break

    if opcoes in ['1','2','3','4']:
        valor1= float(input('digite o primeiro número:'))
        valor2= float(input('digite o Segundo número:'))

    if opcoes == '1':
          print(f'Resultado: {soma(valor1,valor2)}')

    elif opcoes == '2':
      print(f'Resultado: {subtracao(valor1,valor2)}')

    elif opcoes == '3':
      print(f'Resultado: {multiplicacao(valor1,valor2)}')

    elif opcoes == '4':
            print(f'Resultado: {divisao(valor1, valor2)}')


    else:
      print("Opção invalida. Tente novamente")




