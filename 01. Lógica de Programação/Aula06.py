#Conteudo da aula: formatacao de strings com o metodo format
a = 'A' #0
b = 'B' #1
c = 7.777 #2

#formato = 'a={} b={} c={:.2f}'.format(a,b,c) #Padrao de ordem format: {0} {1}...
#print(formato)

string = 'a={} b={nome2} c={nome3}'
formato = string.format(a, nome2=b, nome3=c)

print(formato)
print(f'a = {a}, b = {b}, c = {c}')