#Crie uma função que retorna se um número é maior ou menor do que 10.

def exe51(n):

    resultado = ''

    if n < 10:
        resultado = print('Valor menor que 10!')
    else:
        resultado = print('Valor maior que 10!')
    return resultado

n1 = exe51(20)
print(n1)