'''
Estudando mais métodos
    append = adiciona um item ao final da lista
    insert = adiciona um item no indice escolhido
    pop = remove ultimo item da lista
    del = apaga um indice
    clear = limpa a lista
    extend = estende a lista
'''

lista = [10, 20, 30, 40, 50]

lista.append(60) #adiciona 60
lista.pop() #remove 60
del lista[4] #remove item 4(50)
#lista.clear()
#lista.extend()
lista.insert(0, 5) #dois argumentos: indice/valor
print(lista)


lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

lista3 = lista1 + lista2
lista1.extend(lista2) #extende em si nao retorna nada, mas atribui um valor

print(lista3)
print(lista1)