#Escreva um loop while que vai de 20 a 0. Quando encontrar o número 5 cancele o loop.

num = 20

while num >= 0:
    print(num)
    num -= 1

    if num == 5:
        break