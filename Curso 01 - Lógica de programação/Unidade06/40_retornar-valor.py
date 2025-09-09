#As funções normalmente retornam valores, por meio da instrução return.
    #O retorno pode ser inserido em uma variável e utilizado posteriormente

def saudacao(nome):
    return (f'Olá, {nome}.')

sds = saudacao('Arisio')
print(sds)
print(sds + ' Tudo bem? ')

def soma(a, b):
    return (a + b)

s1 = soma(5, 5)
print(s1)