#Se atribuirmos o valor da copia de uma lista, a segunda será uma referencia da primeira
# O que pode ser um grande problema!

lista = [1, 2, 3]

nova_lista = []

nova_lista = lista 

print(lista)
print(nova_lista)

nova_lista[0] = 100

print(nova_lista)
print(lista)