'''
13 - Faça um programa que receba a temperatura média
de cada mês do ano e armazene-as em uma lista. Após isto,
calcule a média anual das temperaturas e mostre todas as
temperaturas acima da média anual, e em que mês elas ocorreram
(mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
'''

meses = [ 
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro"
]
medias = []

for i in range(12):
    media = float(input(f"Média de temperatura de {meses[i]}: "))
    medias.append(media)

mediaAnual = (sum(medias) / len(medias))

for i in range(12):
    if(medias[i] > mediaAnual):
        print(meses[i])