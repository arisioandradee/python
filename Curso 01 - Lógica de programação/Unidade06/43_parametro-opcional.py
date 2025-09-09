#As funções podem ser criadas com parâmetros opcionais, ou seja, um valor pode já estar preenchido.
    #Podemos utilizar a função sem passar o valor do parametro
        #def teste(x = 10): / print(x)

def imprimeNome(nome = 'Matheus'):
    print(f'Olá, {nome}')


imprimeNome()
imprimeNome('Arisio')
imprimeNome('Andrade')