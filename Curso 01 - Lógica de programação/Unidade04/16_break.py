#Com o BREAK podemos interromper uma repetição
    #Fará com que o loop seja cancelado totalmente!

num = 0

while num < 10:
    print(num)
    num += 1

    if num == 5:
        break