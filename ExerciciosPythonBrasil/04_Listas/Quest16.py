'''
16 - Utilize uma lista para resolver o problema a seguir.
Uma empresa paga seus vendedores com base em comissões.
O vendedor recebe $200 por semana mais 9 por cento de suas
vendas brutas daquela semana.
Por exemplo, um vendedor que
teve vendas brutas de $3000 em uma semana recebe $200 mais 9
por cento de $3000, ou seja, um total de $470.
Escreva um programa (usando um array de contadores) que determine quantos
vendedores receberam salários nos seguintes intervalos de valores:

$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante

Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário,
sem fazer vários ifs aninhados.
'''
intervalos = [
    "200-299", 
    "300-399", 
    "400-499", 
    "500-599", 
    "600-699",
    "700-799", 
    "800-899", 
    "900-999", 
    "1000+"
]

salarios = []

while True:
    vendas = float(input("Vendas brutas da semana (0 para sair): "))
    
    if vendas == 0:
        break
    
    salario = 200 + 0.09 * vendas  
    salarios.append(salario)       

contadores = [0] * len(intervalos)

for salario in salarios:
    indice = int(salario // 100) - 2
    if indice > 8:
        indice = 8
    contadores[indice] += 1

print("\nDistribuição de salários:")
for i in range(len(intervalos)):
    print(f"${intervalos[i]}: {contadores[i]} vendedores")
    
