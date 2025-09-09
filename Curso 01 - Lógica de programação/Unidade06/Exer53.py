#Escreva uma função que receba uma lista de números, a função deve retornar apenas os pares da lista

def recebe_lista(lista):
    for n in lista:
        if(n % 2 == 0):
            print(n)

lista1 = [1, 2, 3, 4, 5]
checar_lista = recebe_lista(lista1)
print(checar_lista)