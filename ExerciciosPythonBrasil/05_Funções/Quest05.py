'''
5 - Faça um programa com uma função chamada soma_imposto. 
A função possui dois parâmetros formais: taxa_imposto, que é a quantia de imposto
sobre vendas expressas em porcentagem, e custo, que é o custo de um item antes do imposto
A função "altera" o valor de custo para incluir o imposto sobre vendas.
'''

def soma_imposto(taxa_imposto, custo):
    novoCusto = custo + (custo * (taxa_imposto/100))
    return novoCusto
    
taxa = float(input("Informe o valor da taxa(%): "))
custo = float(input("Informe o custo do produto: "))

print(f'O novo custo do produto é: R${soma_imposto(taxa,custo)}')