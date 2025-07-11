'''
11 - Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
'''

vetorA = []
vetorB = []
vetorC = []
vetorD = []

for i in range(10):
    item = input('Digite um valor para o 1° vetor: ')
    vetorA.append(item)

for i in range(10):
    item = input('Digite um valor para o 2° vetor: ')
    vetorB.append(item)

for i in range(10):
    item = input('Digite um valor para o 3° vetor: ')
    vetorC.append(item)

for i in range(10):
    vetorD.append(vetorA[i])
    vetorD.append(vetorB[i])
    vetorD.append(vetorC[i])

print(vetorD)