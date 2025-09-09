#Crie um dicionário chamado carro com os dados da foto e adicione a chave teto solar com valor 1
    #Delete motor e janelas, imprima o resultado final


carro = {
    'pneu': 4,
    'portas': 2,
    'motor': 1,
    'janelas': 4
}

print(carro) #Dicionário normal!

carro['teto_solar'] = 1
print(carro) #Dicionário com teto solar adicionado!

del carro['motor']
del carro['janelas']
print(carro) #Dicionário final!

