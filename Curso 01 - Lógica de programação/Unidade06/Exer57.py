#Crie uma função que recebe uma sequência de parâmetros númericos, multiplique todos e exiba o resultado

def multiplicacao(*nums):
    resultado = 1

    for n in nums:
        resultado *= n
    return resultado


m1 = multiplicacao(5, 5, 5, 5)
print(m1)