#Criar classe Carro com marca, valor, número de portas e tanque de gasolina.
    #Crie um método que abastece o tanque de gasolina
        #Crie um método dirigir que remove a gasolina baseado em uma km rodada


class Carro:
    def __init__(self, marca, valor, num_portas, tanque):
        self.marca = marca
        self.valor = valor
        self.num_portas = num_portas
        self.tanque = tanque

    def abastecer(self, litros):
        self.tanque += litros

    def dirigir(self,km):
        #self.km = km
        km_por_litro = 10
        self.tanque -= (km / km_por_litro)


carro1 = Carro('VW', 45000, 4, 30.0)

carro1.abastecer(200.0)
print(carro1.tanque)
carro1.dirigir(10)
print(carro1.tanque)