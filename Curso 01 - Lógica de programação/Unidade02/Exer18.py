#Crie um programa que receba um deposito e depois faça saque, como um banco.

deposito = float(input('Digite o valor que deseja depositar: '))
print(f'Seu saldo é R${deposito:.2f}')

saque = float(input('Digite o valor que deseja sacar: '))

saldo = deposito - saque

print(f'Após o saque de R${saque:.2f}, seu saldo ficou R${saldo:.2f}')
