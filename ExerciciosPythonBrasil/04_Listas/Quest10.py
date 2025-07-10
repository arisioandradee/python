'''
10 - Faça um Programa que leia dois vetores com 10 elementos cada.
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos
pelos elementos intercalados dos dois outros vetores.
'''
vetorA = []
vetorB = []
vetorC = []

for i in range(10):
    item = input('Digite um valor para o 1° vetor: ')
    vetorA.append(item)

for i in range(10):
    item = input('Digite um valor para o 2° vetor: ')
    vetorB.append(item)

for i in range(10):
    vetorC.append(vetorA[i])
    vetorC.append(vetorB[i])

print(vetorC)