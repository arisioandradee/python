#Podemos usar a função find() que possibilita buscar em strings, a resposta será o indice da ocorrencia
    #caso não seja encontrada receberemos o valor -1

frase = 'Eu quero encontrar o peixe'

print(frase.find('peixe')) #retorna o indice que encontrou
print(frase.find('Eu'))
print(frase.find('tubarao')) #retorna -1 pois nao existe