"""
Exercício 02 da seção de listas da Python Brasil:

Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

    >>> inverter_vetores([0,1,2,3,4,5,6,7,8,9])
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

    >>> inverter_vetores([10,14,16,26,36,46,58,24,35,40])
    [40, 35, 24, 58, 46, 36, 26, 16, 14, 10]
"""

numeros = []

for i in range(10):
    numero = int(input('Informe um número: '))
    numeros.append(numero)

novaLista = sorted(numeros)
novaLista.sort(reverse=True)

print(f'Lista de números na ordem de envio:  {numeros}')
print(f'Lista de números na ordem reversa:  {novaLista}')