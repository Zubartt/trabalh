'''Desenvolver um programa que pergunte um número inteiro de 3 algarismos e apresente como resultado
somente o algarismo das centenas.'''

numero = int(input("Digite um número inteiro de 3 algarismos: "))
centenas = numero // 100
print(f"O algarismo das centenas é: {centenas}")