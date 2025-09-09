#podemos adicionar a um dicionário criando nova chave e atribuir um valor, para deletar usamos o del.
    #del dicionario["chave"]

carro = {
    "portas":4,
    "janelas":4,
    "motor":2.0,
    "teto_soalr":True,
    "cambio": 'Automatico'
}

print(carro)

carro["aro"] = 24 #Adicionando chave
print(carro)

del carro['aro'] #Removendo chave adicionada anteriormente
print(carro)