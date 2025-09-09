#Encapsulamento é outro recurso da POO.
    #A ideia é criar atributos privados, que não podem ser alterados
        #Fazemos isto em Python com __ ou __ na frente dos métodos ou variaveis


class Aviao:
    __asas = 2

    def __init__(self, marca):
        self.marca = marca

    def mostrar_asas(self):
        print(f'O avião tem {self.__asas} asas')

aviao1 = Aviao('gol')

print(aviao1.marca)
#print(aviao1.__asas) #AttributeError: 'Aviao' object has no attribute '__asas' (nao deixa acessar pois está "privado")
aviao1.mostrar_asas()
        