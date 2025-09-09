#Textos são chamados de strings e ficam entre aspas.

profissao = 'programador'
nome = 'Arisio'
valor = 50.25

#Função len retorna o tamanho de uma string
print(len(profissao)) 

#Acessando caracteres de uma string. obs: o cursor começa por 0
print(profissao[3]) 

#Concatenação de strings, podemos juntar strings com +
print(nome + ' é um ' + profissao) 

#Strings dinâmicas, usamos o símbolo % (d: int, s: string, f: float)
print('Olá, meu nome é %s' % nome)
print(f'Olá, meu nome é {nome}')

#Strings com decimais
print(f'{valor:.2f}')
print(f'{valor:.1f}')

#Decomposição de Strings
print(nome[2:5]) #Arisio = isi
print(nome[:3]) #Pega do valor da direita para trás
print(nome[3:]) #Pega do valor da esquerda para frente
print(nome[0:-5]) #conta do valor da esquerda e tira a quantidade da direta
