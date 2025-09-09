#Crie uma lista com listas dentro dela
    #ideia: produdos com nome, cor e preço

lista1 = ['Pano de chão', 'Cinza', 5]
lista2 = ['Vassoura', 'Vermelha', 20]
lista3 = ['Rodo', 'Azul', 15]

produtos = [lista1, lista2, lista3]

print(produtos)

for produto in produtos:
    print(f'O produto é {produto[0]} possui a cor {produto[1]} e custa R${produto[2]}')

          