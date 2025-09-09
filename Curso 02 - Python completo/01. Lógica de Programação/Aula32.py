'''
Cuidados com dados mutáveis
    copiando o valor (imutáveis)
    aponta para o mesmo valor na memória (mutável)
'''
nome = 'Arisio'
nome = 'Andrade'
print(nome)
#os valores possuem ID's diferentes na memória, quando chamamos a variavel apontamos para o id

lista_a = ['Arisio', 'Andrade']
lista_b = lista_a #lista a e b apontam para a msm coisa na memoria
