#Podemos checar se uma chave existe em um dicionário usando o operador in, a resposta é em boolean

livros = {
    'Maquiavel': 300,
    'A arte da guerra': 320,
    'FBI': 180
}

print(livros)
print('Maquiavel' in livros)
print('Erro' in livros)

if 'Maquiavel' in livros:
    print('Chave existe!')
else:
    print('Chave não existe!')