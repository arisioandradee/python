'''
19 - Uma empresa de pesquisas precisa tabular os resultados da
seguinte enquete feita
a um grande quantidade de organizações:

"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro

Você foi contratado para desenvolver um programa que leia o resultado da
enquete e informe ao final o resultado da mesma. O programa deverá ler os
valores até ser informado o valor 0, que encerra a entrada dos dados.
Não deverão ser aceitos valores além dos válidos para o programa (0 a 6).
Os valores referentes a cada uma das opções devem ser armazenados num vetor.
Após os dados terem sido completamente informados, o programa deverá calcular
a percentual de cada um dos concorrentes e informar o vencedor da enquete.
O formato da saída foi dado pela empresa, e é o seguinte:

Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos,
correspondendo a 40% dos votos.
'''
respostas = [0] * 6
sistemas = [
    "Windows Server",
    "Unix",
    "Linux",
    "Netware",
    "Mac OS",
    "Outro"
]

while True:
    resposta = int(input("Escolha uma opção(1-6): "))
    
    if resposta == 0:
        break
    
    if resposta < 0 or resposta > 6:
        print("Voto inválido, não será computado!")
        continue
    
    respostas[resposta - 1] += 1 

totalVotos = sum(respostas)
    
print("Sistema Operacional   -   Votos  -    %")
print("-" * 50)
for i in range(6):
    votos = respostas[i]
    if(votos > 0):
        percentual = (votos / totalVotos) * 100
        print(f"{i} - {sistemas[i]:<25} {votos^5} {percentual:2f}")
print("-" * 50)    