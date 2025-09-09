# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
pessoa = {
    'nome': 'Arisio',
    'sobrenome': 'Andrade',
    #'idade': 20,
}
pessoa.setdefault('idade', 0) #adicionar um valor padrao para chaves que pode ou n existir

print(pessoa['idade'])
print()

print(len(pessoa))
print(list(pessoa.keys())) #chaves
print(list(pessoa.values())) #valores
print(list(pessoa.items())) #chaves e valoress

#for chave, valor in pessoa.items():
#    print(chave,valor)