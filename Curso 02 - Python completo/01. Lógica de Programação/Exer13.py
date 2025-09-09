#Faça uma lista de compra com listas
    #o usuário deve ter a possibilidade de inserie, apagar e listar valores da sua lista
    #não permita que o programa quebre com erros de indices inexistentes na lista

lista = []

while True:
    print('Selecione uma opção: ')
    escolha = input('[i]nserir / [a]pagar / [l]listar / [s]air: ')
    escolha.lower()

    if escolha == 'i':
        valor = input('Valor: ')
        lista.append(valor)
        continue
    elif escolha == 'a':
        apagar = int(input('Escolha o indice para apagar: '))
        del lista[apagar]
    elif escolha == 'l':
        lista_enumerada = list(enumerate(lista))
        print(lista_enumerada)
    elif escolha == 's':
        break
    else:
        break