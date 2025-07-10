'''
6 - Faça um Programa que peça as quatro notas de 10 alunos, calcule e
armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0.
'''
medias = []
aprovados = 0

for i in range(10):
    nota1 = float(input('Digite sua 1° nota: '))
    nota2 = float(input('Digite sua 2° nota: '))
    nota3 = float(input('Digite sua 3° nota: '))
    nota4 = float(input('Digite sua 4° nota: '))

    media = (nota1 + nota2 + nota3 + nota4) / 4
    medias.append(media)

for media in medias:
    if media >= 7.0:
        aprovados += 1
    
print(f'Foram aprovados {aprovados} alunos!')