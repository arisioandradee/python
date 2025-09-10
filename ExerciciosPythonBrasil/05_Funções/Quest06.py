'''
6 - Faça um programa que converta a notação de 24 horas para a notação de 12 horas. 
Por exemplo, o programa deve converter 14:25 em 2:25 P.M.
A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer
a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para
A.M. e ‘P’ para P.M.

Assim, a função para efetuar as conversões terá um parâmetro formal para registrar 
se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para
novos valores de entrada todas às vezes que desejar.
'''

def converterNotacao(hora24, minuto24):
    if hora24 == 0:
        return 12, minuto24, 'A' 
    elif hora24 == 12:
        return 12, minuto24, 'P'  
    elif hora24 > 12:
        return hora24 - 12, minuto24, 'P'  
    else:
        return hora24, minuto24, 'A'

def exibirConversao(h, m, periodo):
    sufixo = 'A.M.' if periodo == 'A' else 'P.M.'
    print(f"{h}:{str(m).zfill(2)} {sufixo}")

while True:
    print("\nConversor de horário 24h → 12h")
    try:
        hora = int(input("Informe a hora (0 a 23): "))
        minuto = int(input("Informe os minutos (0 a 59): "))

        if not (0 <= hora <= 23 and 0 <= minuto <= 59):
            print("Horário inválido. Tente novamente.")
            continue

        h12, m12, periodo = converterNotacao(hora, minuto)
        exibirConversao(h12, m12, periodo)

    except ValueError:
        print("Entrada inválida. Use apenas números inteiros.")
        continue

    repetir = input("Deseja converter outro horário? (s/n): ").strip().lower()
    if repetir != 's':
        print("Encerrando o programa.")
        break