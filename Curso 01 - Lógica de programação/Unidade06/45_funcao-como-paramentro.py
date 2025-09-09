#Podemos inserir funções como parâmetros para outras funções, assim, reaproveitando o código


def soma (a, b):
    return a + b

def sub(a, b, s):
    resultado = s(a, b)
    return resultado


a = sub(5, 5, soma)

print(a)