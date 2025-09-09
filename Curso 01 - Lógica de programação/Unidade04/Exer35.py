#Crie um programa que receba um valor inteiro(dinheiro) e imprime na tela o número de cédulas entregues ao usuário
    #ex: 60(1 de 5 e 1 de 10) | as notas disponiveis são 100,50,20,10

valor = int(input('Digite o valor que deseja sacar: '))

nota_100 = 0
nota_50 = 0
nota_20 = 0
nota_10 = 0

while valor > 0:
    while valor >= 100:
        nota_100 += 1
        valor = valor - 100

    while valor >= 50:
        nota_50 += 1
        valor = valor - 50

    while valor >= 20:
        nota_20 += 1
        valor = valor - 20

    while valor >= 10:
        nota_10 += 1
        valor = valor - 10
    
print(f'Notas de 100:{nota_100} | Notas de 50:{nota_50} | Notas de 20:{nota_20} | Notas de 10:{nota_10}')