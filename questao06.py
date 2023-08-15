'''Desenvolver um programa que pergunte dois valores numéricos inteiros e apresente o valor da diferença entre o
maior valor e o menor valor lido.'''

valor1 = int(input("Informe o primeiro valor inteiro: "))
valor2 = int(input("Informe o segundo valor inteiro: "))

if valor1 > valor2:
    maior_valor = valor1
    menor_valor = valor2
else:
    maior_valor = valor2
    menor_valor = valor1

diferenca = maior_valor - menor_valor

print(f"A diferença entre o maior valor ({maior_valor}) e o menor valor ({menor_valor}) é {diferenca}.")