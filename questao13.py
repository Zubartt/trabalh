'''Desenvolver um programa que pergunte 3 valores (variáveis a, b e c) e ao final apresente-os dispostos em ordem
crescente'''

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# 1- A tem que ser menor que B
if ( a > b ):
    aux = a
    a = b
    b = aux
# garantido até aqui que entre A e B, o menor está em A
# 2- A tem que ser menor que C
if ( a > c ):
    aux = a
    a = c
    c = aux
# garantido até aqui que A é o menor dos 3
# agora é necessário garantir que B seja menor que C
if ( b > c ):
    aux = b
    b = c
    c = aux
# garantido até aqui que entre B e C, o B é menor, ou seja, o C é o maior de todos

print (f"Ordem crescente: {a}, {b} e {c}")