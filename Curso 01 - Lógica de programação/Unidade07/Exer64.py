#Crie uma classe Mamífero com propriedades de mamíferos
    #Herde os detalhes desta classe e crie novas para Cachorro e Gato
        #Crie objetos destas classes que herdam de mamiferos

class Mamiferos:
    def __init__(self, pata, calda, orelha):
        self.pata = pata
        self.calda = calda
        self.orelha = orelha
    
class Cachorro(Mamiferos):
    def __init__(self, pata, calda, orelha, fucinho): 
        super().__init__(pata, calda, orelha) #erdando ded mamiferos
        self.fucinho = fucinho

class Gato(Mamiferos):
    def __init__(self, pata, calda, orelha, pelo):
        super().__init__(pata, calda, orelha)
        self.pelo = pelo


animal1 = Mamiferos(4, True, 2)
animal2 = Cachorro(4, True, 2, True)
animal3 = Gato(4, True, 2, True)

print(animal2.fucinho)