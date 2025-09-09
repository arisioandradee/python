#Classe são moldes de objetos, então vamos criar uma classe que pode originar diversos objetos
    #Podemos adicionar propriedades e métodos a uma classe, que serão utilizados por seus objetos

class Pessoa:
    def __init__(self, nome, idade): #selfe = ele mesmo / o proprio objeto
        self.nome = nome
        self.idade = idade