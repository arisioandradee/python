#Escreva um função que recebe uma lista de números e calcule a média nos números da lista

def media(lista):

    total = 0
    media = 0

    for n in lista:
        total += n

    media = total / n
    return media

l1 = [1, 2, 3, 4, 5]

medial1 = media(l1)
print(medial1)