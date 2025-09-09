#Podemos verificar o maior valor de uma lista facilmente com o for, 
    #faremos um loop e checamos se o valor atual é maior que o maior valor

lista = [1, 2, 3, 4, 5]

maior_valor = 0

for n in lista:
    if n > maior_valor:
        maior_valor = n

print(maior_valor)         