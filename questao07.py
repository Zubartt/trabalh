'''Desenvolver um programa que pergunte um valor inteiro positivo ou negativo, e exiba como resposta o módulo
deste valor, ou seja, o número lido como sendo positivo'''

num = int(input("Digite um valor inteiro: "))
if (num < 0):
    positivo = num * -1
    print(f"o modulo é {positivo}")
else:
    print(f"o modulo é {num}")