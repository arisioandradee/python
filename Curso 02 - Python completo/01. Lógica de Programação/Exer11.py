'''
Faça um jogo paraa o usuário adivinhar qual a palavra secreta
Você vai propor uma palavra secreta qualquer e pedir para o usuario digitar uma letra
Se a letra estiver na palavra, exiba a letra, se não, exiba *
Faça uma contagem de tentativas do usuário
'''
palavra = 'fortaleza'
letras_acertadas = ''
cont = 0

while True:
    letra = input('Digite uma letra: ')
    
    if len(letra) != 1:
        print('Digite apenas uma letra!')
        continue

    cont += 1

    if letra in palavra:
        letras_acertadas += letra

    palavra_formada = ''
    for letra_secreta in palavra:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra:', palavra_formada)

    if palavra_formada == palavra:
        print('Você ganhou, parabéns!')
        print(f'A palavra era: {palavra}')
        print(f'Tentativas: {cont}')
        break

