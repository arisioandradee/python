'''
Iterável = str, range, etc...
Iterador = quem sabe entregar um valor por vez
next = me entregue o proximo valor
iter = me entregue o valor do iterador
'''
# texto = 'Arisio'
# numeros = range(0, 100, 8)

# for numero in numeros:
#     print(numero)

texto = iter('Arisio') #iterador

# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__()) #letra em letra
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())

print(next(texto))
