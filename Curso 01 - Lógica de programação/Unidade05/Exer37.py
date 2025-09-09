#Criar uma lista vázia e o usuário digitar os valores dela:
lista = [0, 0, 0, 0, 0]

i = 0

while i < 5:
    num = int(input('Digite um número: '))
    lista[i] = num
    i += 1 

print(lista)