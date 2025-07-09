# isinstace - para saber se objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

for valor in lista:
    if(isinstance(valor, int)):
        print(f'O valor {valor} é do tipo inteiro!')
    elif(isinstance(valor, str)):
        print(f'O valor {valor} é do tipo String!')
    elif(isinstance(valor, float)):
        print(f'O valor {valor} é do tipo float!')
    elif(type(valor) is bool):
        print(f'O valor {valor} é do tipo boolean!')
    elif(isinstance(valor, list)):
        print(f'O valor {valor} é do tipo lista!')
    elif(isinstance(valor, tuple)):
        print(f'O valor {valor} é do tipo tupla!')
    elif(isinstance(valor, set)):
        print(f'O valor {valor} é do tipo set!')
    elif(isinstance(valor, dict)):
        print(f'O valor {valor} é do tipo dicionario!')