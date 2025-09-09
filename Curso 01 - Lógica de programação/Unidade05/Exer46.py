#Crie um programa que verifique o menor valor de uma lista

lista = [1, 2, 3, 4, 5]

menor_valor = lista[0] # ou poderia ser menor_valor = 9999999 já que 0 seria menor que 1

for n in lista:
    if n < menor_valor:
        menor_valor = n

print(menor_valor)