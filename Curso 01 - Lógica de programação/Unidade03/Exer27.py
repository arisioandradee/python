#Faça um programa que recebe a renda do usuário que tenta adquirir um cartão de crédito:
    # Menor que 2000 = 1000 de limite
    # Menor que 4000 = 2000 de limite
    # Menor que 6000 = 3000 de limite
    # Menor que 1000 = falar com o gerente

renda = float(input('Digite sua renda: '))

if renda < 6000 and renda >= 4000:
    print('Você conseguiu R$3000.00 de limite!')
elif renda < 4000 and renda >= 2000:
    print('Você conseguiu R$2000.00 de limite!')
elif renda < 2000 and renda >= 1000:
    print('Você conseguiu R$1000.00 de limite!')
elif renda < 1000:
    print('Falar com o gerente!')
else:
    print('Erro!')