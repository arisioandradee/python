#args -> argumentos não nomeados
# *args(empacotamento e desempacotamento)

x, y, *resto = 1,2,3,4

#def soma(x, y):
#    return x + y

def soma (*args):
    total = 0
    for numero in args:
        total += numero
        #print(total)
    print(total)

soma(1,2,3,4,5)
 
soma1 = soma(4,5,6)
soma2 = soma(10,20,30)
