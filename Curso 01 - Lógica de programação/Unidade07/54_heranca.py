#Herança é onde uma classe herda as propriedades e métodos de outra
    #obs: a classe que vai herdar deve receber como parâmetro a classe pai

class Veiculo:
    def __init__(self, rodas, marca):
        self.rodas = rodas
        self.marca = marca
        
    def ligar(self):
        print('Ligando!')

class Carro(Veiculo):
    def __init__(self, rodas, marca, teto_solar):
        super().__init__(rodas, marca) #super = diz que rodas e marca são da classe pai
        self.teto_solar = teto_solar

c1 = Carro(4, 'Ferrari', True)
print(c1.marca)

c1.ligar()
print(c1.teto_solar)