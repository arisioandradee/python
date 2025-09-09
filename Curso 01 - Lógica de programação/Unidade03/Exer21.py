#Crie um programa que recebe o número de rodas que o veiculo possui. Se for maior que 2 paga pedágio

rodas = int(input('Digite a quantidade de rodas do veiculo: '))

if rodas > 2:
    print('Paga pedágio!')

if rodas == 2:
    print('Não paga pedágio!')