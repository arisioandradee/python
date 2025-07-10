'''
9 - Faça um Programa que leia um vetor A com 10 números inteiros,
calcule e mostre a soma dos quadrados dos elementos do vetor.
'''

numeros = []
numerosQuadrados = []
for i in range(10):
    numero = int(input('Digite um número: '))
    numeros.append(numero)

    quadrado = numero ** 2
    numerosQuadrados.append(quadrado)

print(f'Soma dos quadrados dos elementos: {sum(numerosQuadrados)}')