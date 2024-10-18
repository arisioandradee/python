''' exer12
#imprima o indice dos itens de uma lista

lista = [1, 2, 3, 4, 5]
indice = 0
for n in lista:
    print(f'Item: {n}, Indice:{indice}')
    indice += 1
'''
#no python fazemos isso com o enumarate

lista = [1, 2, 3, 4, 5]

#lista_enumerada = list(enumerate(lista))

for indice, num in enumerate(lista):
    #indice, nome = item
    print(indice, num)