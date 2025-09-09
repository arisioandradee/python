#Crie uma função que fala se o número é par ou impar, retorne o resultado

def par_impar(valor):
    if valor % 2 == 0:
        return 'par'
    else:
        return 'impar'
    
valor1 = par_impar(2)
print(valor1)