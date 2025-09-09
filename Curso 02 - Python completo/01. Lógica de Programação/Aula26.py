'''
introdução ao for
texto = 'Python'

i = 0
tamanho_string = len(texto)

while i < tamanho_string:
    print(texto[i], i)
    i += 1
'''
texto = 'Python'
novo_texto = ''

for n in texto:
    print(n)
    novo_texto += f'*{n}'

print(novo_texto)
