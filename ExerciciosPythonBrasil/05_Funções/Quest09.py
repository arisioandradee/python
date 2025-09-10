"""
9 - Faça uma função que retorne o reverso de um número inteiro informado. 
Por exemplo: 127 -> 721.
"""

def reverso(numero):
    return ''.join(reversed(str(numero)))

print(reverso(127))
print(reverso(148))
print(reverso(164))
print(reverso(297))