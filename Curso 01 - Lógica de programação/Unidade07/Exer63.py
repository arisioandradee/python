#Crie uma classe Pessoa com nome e idade.
    #Crie uma classe Super Heroi que herda as caracteristicas básicas da pessoa
        #Crie poderes especiais para o heroi


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Superheroi(Pessoa):
    def __init__(self, nome, idade, super_poder):
        super().__init__(nome, idade)
        self.super_poder = super_poder
    
    def utilizar_poder(self):
        print(f'O heroi usou o poder de {self.super_poder}')
    

p1 = Pessoa('Andrade', 20)

p2 = Superheroi('Andrade', 20, 'Fogo')
p2.utilizar_poder()

