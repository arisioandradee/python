#As strings em Python podem ser facilmente convertidas em lista. A função list quem faz isso
    #Podemos tambem transformar uma lista em string usando a função join

palavra = 'teste'

print(list(palavra)) #['t', 'e', 's', 't', 'e']

lista = ['t', 'e', 's', 't', 'e']

print("".join(lista)) #teste. -> o "" é a forma de separar os elementos