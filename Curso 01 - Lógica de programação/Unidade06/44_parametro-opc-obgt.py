#Podemos ter funções com parâmetros opicionais e obrigatórios, ou seja, cada um é independente do outro.
    #obs: os opcionais devem estar sempre depois dos obrigatórios
        #def teste(x, y = 10) / print(x + y)

def soma_numeros (a, b, c = 10):
    print(a + b + c)

soma_numeros(1, 2, 3) #obrigatorio irá ignorar o 10
soma_numeros(1, 2) #opcional somou o c(10)