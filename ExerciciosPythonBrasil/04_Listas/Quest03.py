"""
Exercício 03 da seção de listas da Python Brasil:

Faça um Programa que receba 4 notas, mostre as notas e a média na tela. 

    >>> mostrar_notas_e_media([0, 1, 2, 3])
    'Notas: 0, 1, 2, 3. Média: 1.5'
    >>> mostrar_notas_e_media([10, 14, 16, 26])
    'Notas: 10, 14, 16, 26. Média: 16.5'
"""

notas = []

for i in range(4):
    nota = float(input(f'Informe sua {i+1}° nota: '))
    notas.append(nota)

media = sum(notas) / len(notas) 
print(f'Notas: {notas}')
print(f'Média: {media}')