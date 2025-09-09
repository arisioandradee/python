#Criar um programa que busca elemento usando o for, quando for encontrado imprima mensagem.

lista = ['Teclado', 'Mouse', 'Headset', 'Monitor']

encontrado = False

objeto = input('Qual objeto você deseja encontrar? ')

for n in lista:
    if n == objeto:
        print('Objeto encontrado! ')
        encontrado = True
        break

if encontrado == False:
    print('Objeto não encontrado!')
