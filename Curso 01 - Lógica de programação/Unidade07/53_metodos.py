#Métodos são funções criadas para os objetos, que podem interagir com o próprio ou outros objetos.
    #obs: a palavra self se trata sempre do objeto em si, iniciamos os métodos com def


class Carro:
    def __init__(self, marca, preco):
        self.marca = marca
        self.preco = preco

    def ligar(self):
        print('Carro ligado')

car1 = Carro('VW', 60000)

print(car1.marca)
car1.ligar()