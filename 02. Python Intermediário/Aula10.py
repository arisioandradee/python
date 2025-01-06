# Manipulando chaves e valores em dicionários
pessoa = {}

#Criar chave
chave = 'nome_completo'

pessoa[chave] = 'Arisio Andrade'
pessoa['sobrenome'] = 'Andrade'
#print(pessoa[chave])

pessoa[chave] = 'Maria Emily' #modificando valor da chave
print(pessoa[chave])

del pessoa['sobrenome']
#print(pessoa.get('sobrenome')) #get busca chave, seu valor padrão é none
if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE!')
else:
    print(pessoa['sobrenome'])