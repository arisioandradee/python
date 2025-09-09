#Criar duas variaveis de lista e criar uma terceira com os elementos das duas anteriores

lista1 = [0, 1, 2, 3, 4]
lista2 = [5, 6, 7, 8, 9]
lista3 = []

i = 0
a = 0

while i < len(lista1):
    lista3.append(lista1[i])
    i += 1

while a < len(lista2):
    lista3.append(lista2[a])
    a += 1

print(lista3)