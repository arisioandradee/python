"""
8 - Faça uma função que informe a quantidade de dígitos de um determinado número 
inteiro informado.
"""

def quantidade(numero):
    numeros =  [int(n) for n in str(numero)]
    contador = 0
    
    for i in numeros:
        contador += 1
    return contador
    
print(quantidade(5020347850))