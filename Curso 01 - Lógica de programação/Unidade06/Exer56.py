#Criar função que recebe outra como parametro. A que vai receber deve receber nome, idade e profissao
    #A função de argumento deve apresentar esses dados em uma strign dinamica



def reune_dados(nome, idade, profissao, fnct):
    apresentacao = fnct(nome, idade, profissao)
    return apresentacao

def apresenta_dados(nome, idade, profissao):
    return (f'O {nome} tem {idade} anos e trabalha como {profissao}')
    

d1 = apresenta_dados('Andrade', 20, 'Programador')
print(d1)