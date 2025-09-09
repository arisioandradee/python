#Repetições aninhadas = podemos inserir um loop dentro do outro.
    #A ordem de execução é de fora pra dentro!

i = 0

while i < 10:
    print(f'i:{i}')

    x = 0

    while x < 5:
        print(f'x:{x}')
        x += 1

    i += 1