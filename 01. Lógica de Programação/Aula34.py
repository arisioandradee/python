#Introdução ao desempacotamento

#nome1, nome2, = ['Arisio', 'Soares', 'Andrade'] / erro: poucas variaveis
#nome1, nome2, nome3 = ['Arisio', 'Soares'] / erro: muitas variaveis

_, nome2, *_ = ['Arisio', 'Soares', 'Andrade']

print(nome2)
print(_) # _ = variavel que não vou usar
