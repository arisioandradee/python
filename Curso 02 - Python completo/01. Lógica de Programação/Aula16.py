#Conteudo da aula: Variaveis, constantes e complexidade de código

# Constante = "variaveis" que não vão mudar

velocidade = 61 # velocidade atual do carro
local_carro = 99 # local do carro na estrada

RADAR_1 = 60 # velocidade máxima do radar(não irá mudar)
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # a distãncia onde o radar funciona

velocidade_ultrapassa = velocidade > RADAR_1
carro_inicio_radar = local_carro >= (LOCAL_1 - RADAR_RANGE)
carro_fim_radar = local_carro <= (LOCAL_1 + RADAR_RANGE) 

if velocidade_ultrapassa:
    print('Carro ultrapassou a velocidade do radar!')
else:
    print('Carro não ultrapassou a velocidade do radar!')

if carro_inicio_radar and carro_fim_radar and velocidade_ultrapassa:
    print('Carro multado!')
else:
    print('Carro não multado!')

''' Código complexo
if velocidade > RADAR_1:
    print('Carro ultrapassou a velocidade do radar!')
else:
    print('Carro não ultrapassou a velocidade do radar!')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and \
        velocidade > RADAR_1:
    print('Carro multado!')
else:
    print('Carro não multado!')
'''