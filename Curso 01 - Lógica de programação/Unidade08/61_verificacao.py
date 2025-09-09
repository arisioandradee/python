#Temos metodos para verificar palavras no inicio e fim de uma string
    #startswith = verifica se inicia com determinada palavra
    #endswith = verifica se termina com determinada palvra

frase = 'Testando inicio e fim da string'

print(frase.startswith('Testando')) #True
print(frase.startswith('Erro')) #False
print(frase.endswith('string')) #True