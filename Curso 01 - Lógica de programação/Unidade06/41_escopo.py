#Quando estamos dentro do bloco de função temos um escopo local.
    #As variáveis desta função não podem ser utilizadas em outra. As variáveis do escopo global podem!

escopo_global = 'Tchau'

def teste():
    teste = 'Olá'
    print(teste)
    print(escopo_global)

teste()

escopo_global = 'Até logo'
print(escopo_global)