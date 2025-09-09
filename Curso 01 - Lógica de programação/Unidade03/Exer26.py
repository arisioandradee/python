#Crie um programa que recebe a categoria, em valor número de um produto:
    #1 - bolsa | 2 - tênis | 3 - mochila. Diferente disso a categoria não foi encontrada!

categoria = int(input('Digite o código da categoria do produto: '))

if categoria == 1:
    print('A categoria é "BOLSA"!')
elif categoria == 2:
    print('A categoria é "TÊNIS"!')
elif categoria == 3:
    print('A categoria é "MOCHILA"!')
else:
    print('Categoria não encontrada! ')