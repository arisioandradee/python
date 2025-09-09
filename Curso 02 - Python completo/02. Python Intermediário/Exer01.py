# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


def multiplicacao(*args):
    resultado = 1
    for numero in args:
        resultado *= numero

    return resultado

multi1 = multiplicacao(2, 2, 2, 2, 2)
print(multi1)
