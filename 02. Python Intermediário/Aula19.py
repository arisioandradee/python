#List comprehension em Python
    #É uma forma rápida de criar listas a partir de iteraveis


#print(list(range(10)))
lista = []

"""for i in range(10):
    lista.append(i)

#print(lista)

lista2 = [
    numero * 2
    for numero in range(10)
]
print(lista2)"""

# Mapeando dados em list comrpehension
produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30},
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    for produto in produtos
]

print(novos_produtos)
print(*novos_produtos, sep='\n')