#Escreva uma função que recebe um dado em texto, se esse dado tiver mais de 20 caracteres retorne que é um texto longo

def texto(txt):
    if len(txt) > 20:
        print('Texto longo!')
    else:
        print('Texto curto!')

texto1 = ('Arisio Andrade está ficando bom em Python!')
texto2 = ('Texto curto!')

checandotxt1 = texto(texto1)
checandotxt2 = texto(texto2)