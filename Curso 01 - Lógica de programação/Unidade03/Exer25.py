#Faça um programa que recebe um valor, se for menos que 10 insira mensagem alertando que precisa ser maior
    #Depois, verifique se o valor é menor que 20 e imprima a multiplicação dele por 2.
        #Se não, multiplicado por 5


num = int(input('Digite um valor: '))

if num > 10:
    if num < 20:
        print(num * 2)
    else:
        print(num * 5)
else:
    print('O valor precisa ser maior que 10!')