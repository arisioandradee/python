#Crie um programa que gera um número de 1 a 10, peça para o usuário adivinhar o número e ver se ele acertou ou não


import random

def sorteio(a, b):
    return random.randint(a, b)

nums = sorteio(1, 10)

usu_n = int(input('Digite um valor entre 1 e 10: '))

if usu_n == nums:
    print('Você acertou!')
else:
    print('Você errou!')