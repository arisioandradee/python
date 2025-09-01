'''
22 -
Sua organização acaba de contratar um estagiário para trabalhar no
Suporte de Informática, com a intenção de fazer um levantamento nas
sucatas encontradas nesta área.
A primeira tarefa dele é testar todos
os cerca de 200 mouses que se encontram lá, testando e anotando o estado
de cada um deles, para verificar o que se pode aproveitar deles.

Foi requisitado que você desenvolva um programa para registrar este
levantamento. O programa deverá receber um número indeterminado de entradas,
cada uma contendo: um número de identificação do mouse o tipo de defeito:

necessita da esfera;
necessita de limpeza;
a.necessita troca do cabo ou conector;
a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa.
Ao final o programa deverá emitir o seguinte relatório:

Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
'''
texto = [
    'Necessita da esfera',
    'Necessita de limpeza',
    'Necessita troca do cabo ou conector',
    'Quebrado ou inutilizado'
]

codigos = []
problemas = [0, 0, 0, 0]

while True:
    codigo_problema = int(input('Informe o código do problema: (1-4)'))

    if codigo_problema == 0:
        break

    if codigo_problema < 0 or codigo_problema > 4:
        print('Código inválido, o produto não foi adicionado!')
        continue

    codigos.append(codigo_problema)

for codigo in codigos:
    problemas[codigo-1] += 1

total = sum(problemas)
print(f'\nQuantidade de mouses: {total}\n')
print(f'{"Situação":35} {"Quantidade":12} {"Percentual":10}')

print('Situalçao - Quantidade - Percentual')
for i in range(4):
    percentual = (problemas[i] / total * 100) if total > 0 else 0
    print(f'{i+1} - {texto[i]:30} {problemas[i]:20} {percentual:9.2f}%')