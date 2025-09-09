# Exercicio para edir ao usuário para digitar nome e idade. Depois exibir na tela:
# Seu nome é:
# Seu nome invertido é:
# Seu nome contém(ou não) espaços
# Seu nome tem {n} letras
# A primeira letra do seu nome é:
# A ultima letra do seu nome é:
# Caso nada for digitado: "Desculpe, você deixou campos vázios"

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if not nome and not idade:
    print("Desculpe, você deixou campos vazios!")
else:
    n = (len(nome[::]))
    espaco = ' ' in nome

    print('-' * 10)
    print(f'Seu nome é: {nome}')
    print(f'Sua idade é: {idade}')
    print(f'Seu nome invertido é: {nome[::-1]}')
    print(f'Seu nome possui espaços? {espaco}')
    print(f'Seu nome tem {n} letras!')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A ultima letra do seu nome é: {nome[-1]}')