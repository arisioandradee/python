#Podemos deletar objetos por meio ded "del nome_objeto", apos isso não podemos mais acessar propriedades do objeto

class Pessoa:
    pass

p1 = Pessoa()
p2 = Pessoa()

print(p1)
print(p2)

del p1
print(p1)
print(p2)