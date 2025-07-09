import sys

#Generator Expression, Iterables e Iterators
iterable = ['Eu', 'sou o ', 'Arisio', '__iter__']
iterator = iter(iterable)

for item in iterable:
    print(next(iterator))

    #o iterator esgota os valores, o que resulta em um StopIteration

#Generator são basicamente funções que sabem pausar
    #Não salva todos os números na memória, fica esperando ser utilizado (diferente de uma lista)
    #Porém não é possivel acessar os indices ou len() igual nas listas
generator = (n for n in range(1000)) 
print(sys.getsizeof(generator))

for n in generator:
    print(n)