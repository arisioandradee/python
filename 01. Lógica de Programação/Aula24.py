#Contudo da aula: while/else

string = 'valor'
i = 0

while i < len(string): #quando o while é executado completamente vai pro else!
    letra = string[i]

    print(letra)
    i += 1
else:
    print('o else foi executado!') #um break dentro do while impede o else de ser usado
    #esse formato é pouco utilizado