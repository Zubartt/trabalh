'''Desenvolver um programa que pergunte dois números inteiros, e apresente como resultado se o segundo
número informado é ou não um divisor do primeiro número informado.'''

num1 = int(input("Informe o primeiro número inteiro: "))
num2 = int(input("Informe o segundo número inteiro: "))

if num1 % num2 == 0:
    print(f"{num2} é um divisor de {num1}.")
else:
    print(f"{num2} não é um divisor de {num1}")