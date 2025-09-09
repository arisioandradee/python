#Criar lista com itens, pedir dois itens ao usuario e identificar qual foi encontrado primeiro!

lista = ['Fortaleza', 'Corinthians', 'Flamengo', 'Fluminense']

i = 0

print('Digite os dois times que deseja encontrar: ')
time1 = input()
time2 = input()

while i < len(lista):
    if lista[i] == time1:
        print('O time 1 foi encontrado primeiro! ')
        break
    elif lista[i] == time2:
        print('O time 2 foi encontrado primeiro! ')
        break
    else:
        print('Os times não foram encontrados!')