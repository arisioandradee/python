#podemos criar um loop que busca um elemento em um array
    #if lista[i] == elemennto / print('encontrado')

lista = ['Sofá', 'Televisão', 'Fogão', 'Cama']

i = 0
achou = False

while i < len(lista):
    if lista[i] == 'Cama':
        print('Encontrado!')
        achou = True
        break  # Como já encontrou o elemento, podemos sair do loop
    i += 1

if not achou:
    print('Não encontrado!')
