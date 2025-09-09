#Escreva uma função que desenha uma escada no terminal. Os números de degraus devem ser informados no parametro
    #ex: # / ## / ###...

def criar_escada(degrau):

    i = 1

    while i <= degrau:
        print('#' * i)
        i += 1

criar_escada(5)
