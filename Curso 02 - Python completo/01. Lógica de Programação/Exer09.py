print('1- Soma | 2- Subtração | 3- Multiplicação | 4- Divisão')
print('-' * 30)
print('Obs: digite 0 para encerrar o programa!')

while True:
    escolha = int(input('Digite a operação que deseja realizar: '))

    if escolha == 0:
        print('Programa encerrado!')
        break

    if escolha in [1, 2, 3, 4]:
        v1 = float(input('Digite o primeiro valor: '))
        v2 = float(input('Digite o segundo valor: '))

        if escolha == 1:
            soma = v1 + v2
            print(f'O valor da soma de {v1} + {v2} é {soma}')
        elif escolha == 2:
            subtracao = v1 - v2
            print(f'O valor da subtração de {v1} - {v2} é {subtracao}')
        elif escolha == 3:
            multiplicacao = v1 * v2
            print(f'O valor da multiplicação de {v1} * {v2} é {multiplicacao}')
        elif escolha == 4:
            if v2 == 0:
                print('Não é possível dividir por zero!')
            else:
                divisao = v1 / v2
                print(f'O valor da divisão de {v1} / {v2} é {divisao}')
    else:
        print('Escolha inválida! Por favor, escolha uma opção de 1 a 4 ou digite 0 para sair.')
