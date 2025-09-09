#Em Python é possivel substituir facilmente um método herdado, preciamos declarar ele na classe filha
    #obs: o método da classe filha que vale pros objetos nesse caso, se criar outra ela herda normalmente

class Pessoa:
    def falar(self):
        print('Olá pessoal!')

class Andrade(Pessoa):
    def falar(self):
        print('Olá pessoal, sou o Andrade')

class teste(Pessoa):
    pass

p1 = Andrade()
p1.falar()

p2 = teste()
p2.falar()
        