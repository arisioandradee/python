#Escreva um programa que recebe dois valores. Insira a multiplicação em uma variavel.
    #Se for menor ou igual a 100 imprime uma mensagem que o valor é baixo

n1 = float(input('Digite um valor: '))
n2 = float(input('Digite um valor: '))

resul = n1 * n2

if resul > 100:
    print('O valor é alto!')
else:
    print('O valor é baixo!')