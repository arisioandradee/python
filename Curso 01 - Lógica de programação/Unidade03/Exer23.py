#Crie um programa que receba um salário, se for maior que 1800 imprima que é necessário imposto de renda

salario = float(input('Digite seu salário: '))

if salario > 1800:
    print('É necessário pagar o imposto de renda!')
else:
    print('Não é necessário pagar o imposto de renda!')