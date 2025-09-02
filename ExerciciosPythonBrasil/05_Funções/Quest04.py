'''
4. Faça um programa, com uma função que necessite de um argumento
A função retorna o valor de caractere ‘P’, se seu argumento for positivo,
e ‘N’, se seu argumento for zero ou negativo.
'''

def positivoNegativo(valor):
    if(valor < 0):
        return "N"
    else:
        return "P"
        
print(positivoNegativo(20))
print(positivoNegativo(-20))
print(positivoNegativo(0))
print(positivoNegativo(-1))