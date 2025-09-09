#Introdução ás Generator fuctions em Python
    #generator = (n for n in range(1000)) 

"""def exibir():
    yield 1 #Pausa
    print('Continunando...')
    yield 2 #Pausa
    print('Mais uma vez...')
    yield 3 #Pausa
    print('Finalizando...')
    return 'Acabou!'"""

def exibir(n=0, maximum=10):
    while True:
        yield n #Pausa
        n += 1

        if(n > maximum):
            break

txt1 = exibir()

for i in txt1:
    print(i)