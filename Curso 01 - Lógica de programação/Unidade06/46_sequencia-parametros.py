#Podemos inserir uma série de parâmetros na hora de criar uma função
    #Se estes forem do memso tipo, ajuda a criar uma função que pode processar diversos parametros

def soma_todos(*nums):
    soma = 0
    for num in nums:
        soma += num
    return soma

s = soma_todos(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(s)