#Agora vamos aprender a forma correta de copiar uma lista

lista = [1, 2, 3, 4]

nova_lista = []

nova_lista = lista[:] #retornando todos os valores da primeira lista

nova_lista[1] = 100 #irá alterar apenas a lista 2

print(nova_lista)
print(lista)