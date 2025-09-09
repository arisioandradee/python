'''
Flag (bandeira) marcar um local
none = não valor
is e is not = é ou não é
id = identidade
'''
condicao = True
passou_no_if = None #melhorar declarar antes do if

if condicao:
    passou_no_if = True
    print('Faça algo!')
else:
    #passou_no_if = none
    print('Não faça algo!')

print(passou_no_if, passou_no_if is None) #passou_no_if é None? false
print(passou_no_if, passou_no_if is not None) #passou_no_if não é none? true