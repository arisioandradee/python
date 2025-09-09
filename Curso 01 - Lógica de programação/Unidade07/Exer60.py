#Criar uma classe Carro com as propriedades de porta, motor, sem teto solar, marca, preco

class Carro:
    def __init__(self, porta, motor, teto_solar, marca, preco):
        self.porta = porta
        self.motor = motor
        self.teto_solar = teto_solar
        self.marca = marca
        self.preco = preco


car1 = Carro(4, '2.0', False, 'Fiat', '35.700')

print(f'{car1.porta}.{car1.motor}.{car1.teto_solar}.{car1.marca}.{car1.preco}')

        