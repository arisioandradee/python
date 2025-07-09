"""
Exercício 01 da seção de listas da Python Brasil:
    Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""

numeros = []

for i in range(5):
    numero = int(input('Informe um número: '))
    numeros.append(numero)

print(f'Lista de números: {numeros}')