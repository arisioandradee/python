"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

n1 = input('Digite um número inteiro: ')

if n1.isdigit():
    n1 = int(n1)
    if n1%2 == 0:
        print('O número é par!')
    else:
        print('O número é impar!')
else:
    print('O valor não é um número inteiro!')