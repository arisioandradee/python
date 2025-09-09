# Objeto é um "filho" de uma classe, ele poderá utilizar as propriedades e métodos que foram definidas na classe pai
    #Após sua criação o objeto é independente da classe, podendo alterar as propriedades isoladamente.

class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao


user1 = Pessoa('Andrade', 20, 'Programador')
print(user1) #<__main__.Pessoa object at 0x000001BDC5E69C40>

print(user1.nome)
print(user1.idade)
print(user1.profissao)

print(f'O nome do usuário 1 é {user1.nome}, possui {user1.idade} e trabalha como {user1.profissao}')