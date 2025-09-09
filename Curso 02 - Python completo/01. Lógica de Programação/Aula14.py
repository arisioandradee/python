#Conteudo da aula: Fatiamento de Strings

# 012345678
# Olá Mundo
# Fatiamento [i:f:p] [::] i = inicio, f = fim, p = passo
# Função len: conta caracteres de uma String

variavel = 'Olá mundo'
print(variavel[0:9:4]) #Fatiando do 0 ao 9, indo de 4 em 4
print(variavel[::-1])
print(len(variavel[4:])) #Inicio do fatimaneto : até onde vai o fateamento (se não colocar  ele vai até o final da string)
