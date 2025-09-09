#Podemos iterar nas tuplas como nas listas com for, utilizamos a mesma sintaxe

tupla = (1, 2, 3, 4, 5)

for n in tupla: #é a mesma estrutura pois o python não faz a distinção dos dois tipos de dado
    print(n)

i = 0

while i < len(tupla):
    print(tupla[i])
    i += 1