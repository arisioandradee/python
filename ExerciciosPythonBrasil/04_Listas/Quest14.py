''' 
14 - Utilizando listas faça um programa que faça 5 perguntas para
uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma
classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve
ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
'''
cont = 0
perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

for i in range(5):
    print(perguntas[i])
    resposta = input().lower()
    
    if(resposta == "sim"):
        cont += 1
    
if(cont  == 2):
    print("Suspeita")
elif(cont > 2 and cont < 4):
    print("Cumplice")
elif(cont == 5):
    print("Assassino")
else:
    print("Inocente")