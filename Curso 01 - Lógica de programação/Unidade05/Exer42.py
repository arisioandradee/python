#Criar uma lista de 1 a 10, percorrer com um loop e quando encontrar o elemento 4 remova-o

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

i = 0

while i < len(lista):
    if lista[i] == 4:
        del lista[4]
        i += 1
    else:
        i += 1


print(lista)

  
