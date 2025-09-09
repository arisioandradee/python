'''
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - indices e fatiamentos
Métodos úteis: append, insert, pop, del, clear, extend...
'''

lista = [123, True, 'Arisio Andrade', 1.2, []]

#print(type(lista))
#print(lista[1], type(lista[1]))
#lista[1] = False
#print(lista[1], type(lista[1]))

del lista [4] #deletando item com indice 4 da lista
lista.append(456) #adicionando valor ao final da lista
lista.append(50)
lista.pop() #remove o ultimo elemento(50)
print(lista)