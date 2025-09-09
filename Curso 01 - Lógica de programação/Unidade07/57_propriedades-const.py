#Podemos definir propriedades que não variam de objeto em classe, ou seja, iniciam com um valor fixo
    #basta declarar fora de __self__ com algum valor


class Carro:

    rodas = 4

    def __init__(self, marca):
        self.marca = marca


carro1 = Carro('Ferrari')

print(carro1.marca)
print(carro1.rodas)

    