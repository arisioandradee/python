#Faça um programa que recebe um valor salário, outro como porcentagem de aumento e exiba o valor total após o aumento.

salario = float(input('Digite um salário: '))
aumento = int(input('Digite a porcentagem de aumento: '))

salario += salario * (aumento/100)

print(f'Valor do novo salário: R${salario:.2f}')