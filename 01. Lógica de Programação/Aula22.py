#Conteudo da aula: pulando linha no while (continue)

contador = 0

while (contador < 100):
    contador += 1

    if contador == 10:
        print('Não vou mostrar o 10!')
        continue

    if contador >= 20 and contador <= 25:
        print(f'Não vou mostrar o {contador}')
        continue

    print(contador)

    if contador == 40:
        break

print('Acabou o while!')