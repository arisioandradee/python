#Crie funções que duplicam, triplicam e quadriplicam um numero

def multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = multiplicador(2)
triplicar = multiplicador(3)

print(duplicar(2))
print(triplicar(3))