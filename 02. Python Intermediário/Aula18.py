#Empacotamento e desempacotamento de dicionários

a, b =  1, 2
a, b = b, a
#print(a, b)



#(a1, a2), b = pessoa.items()
#print(a1, a2)

#for chave, nome in pessoa.items():   
    #print(chave, nome)

pessoa = {
    'nome': 'Arisio',
    'sobrenome': 'Andrade',
}

dados_pessoa = {
    'idade': 18,
    'altura': 1.80,
}

print(pessoa, dados_pessoa)

dicionarioGeral = {**pessoa, **dados_pessoa}
print(dicionarioGeral)

for valor in dicionarioGeral.values():
    print(valor)