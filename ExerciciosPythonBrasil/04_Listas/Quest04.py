'''
Faça um Programa que leia um vetor de 10 caracteres, e diga
quantas consoantes foram lidas.
Imprima as consoantes.
'''
letras = []
letrasVogais = ['a', 'e', 'i', 'o', 'u']
consoantes = 0

for i in range(10):
    letra = input(f'Informe a {i+1}° letra: ')
    letras.append(letra)

    if(letra not in letrasVogais):
        consoantes += 1

print(f'Foram lidas {consoantes} consoantes')