'''
8 - Faça um Programa que peça a idade e a altura de 5 pessoas,
armazene cada informação no seu respectivo vetor.
Imprima a idade e a altura na ordem inversa a ordem lida.
'''

idades = []
alturas = []

for i in range(10):
    idade = int(input('Informe sua idade: '))
    altura = float(input('Informe sua altura: '))
    idades.append(idade)
    alturas.append(altura)

for item in idades, alturas:
    print(item[::-1])