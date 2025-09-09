#Elif é a forma que temos de escrever outros ifs antes do else

nome = input('Digite seu nome: ')

if nome == 'Arisio':
    print('O usuário é um administrador!')
elif nome == 'Andrade':
    print('O usuário é um programador!')
else:
    print('O usuário é comum!')