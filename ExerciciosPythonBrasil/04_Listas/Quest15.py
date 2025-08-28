"""
15 - Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados,
um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem
"""
contador1, contador2 = 0, 0
notas = []

while True:
    nota = float(input("Nota: "))
    
    if(nota == -1):
        break
    
    notas.append(nota)
    
somaNotas = sum(notas)
mediaNotas = somaNotas / len(notas)
    
for nota in notas:
    if(nota > mediaNotas):
        contador1 += 1
        
for nota in notas:
    if(nota < 7):
        contador2 += 1
    
print("-" * 50)    
print(f"Quantidade de notas: {len(notas)}")
print(*notas)
print(*notas[::-1])
print(f"Soma das notas: {somaNotas}")
print(f"Média das notas: {mediaNotas}")
print(f"Notas acima da média: {contador1}")
print(f"Notas abaixo de 7: {contador2}")