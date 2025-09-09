#Crie uma lista com 5 notas, faça um looping que calcule as médias e imprima o resultado!

notas = [10, 8.8, 6.4, 5.2, 9.8]

i = 0
soma = 0

while i <= 5:
    soma = soma + notas[1]
    i += 1

media = soma / 5

print(f'A médias dos resultads é: {media:.2f}')