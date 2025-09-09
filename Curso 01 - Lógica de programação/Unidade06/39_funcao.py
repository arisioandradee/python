#Já usamos diversas funções no Python: print, len, float, int, input.
    #A ideia principal é criar um bloco de código reutilizável, assim podemos chamar a função em qualquer lugar do cód.

def digaOi(nome): #basta apenas alterar nessa parte, não no código todo
    print(f'Olá, {nome}')

nome = input('Digite um nome: ')
digaOi(nome)
digaOi('Andrade')
digaOi('Teste')