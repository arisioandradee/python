#Exercicio básico saber qual é o maior entre dois valores

valor_1 = input("Digite o primeiro valor:")
valor_2 = input("Digite o segundo valor:")

if(valor_1 > valor_2):
    print(f'O valor {valor_1} é maior do que o {valor_2}!')
elif(valor_2 > valor_1):
    print(f'O valor {valor_2} é maior do que o {valor_1}!')
else:
    print(f'Os valores {valor_1} e {valor_2} são iguais!')
