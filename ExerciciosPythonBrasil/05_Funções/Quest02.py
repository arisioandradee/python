'''
2 - Faça um programa para imprimir:
1
1   2
1   2   3
1   2   3   ...  n
'''

def imprimir(n):
    return [str(i) for i in range(1, n + 1)]

n = int(input("Informe um número: "))

for i in range(1, n + 1):
    print(' '.join(imprimir(i)))
