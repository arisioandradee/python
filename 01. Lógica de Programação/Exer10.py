frase = 'O rato roeu a roupa do rei de roma'

frase = frase.lower()

i = 0
mais_vezes = 0
letra_apareceu_mais = ''

# Contagem das letras
for letra in frase:
    if letra.isalpha():  # Verifica se é uma letra
        mais_vezes_atual = frase.count(letra)
        if mais_vezes_atual > mais_vezes:
            mais_vezes = mais_vezes_atual
            letra_apareceu_mais = letra

print("A letra que mais apareceu foi:", letra_apareceu_mais, "com", mais_vezes, "vezes.")
