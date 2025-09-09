#Python tem muitos métodos mágicos(__metodo__), um dele é o __str__:
    #Ele serve para imprimir uma representação em string do que desejamos

class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return (f'O nome do usuário é {self.nome}, possui {self.idade} anos e trabalha como {self.profissao}')
    

p1 = Pessoa('Andrade', 20, 'Programador')

print(p1.__str__()) #tem que dar print pois é uma string que vem de um return 