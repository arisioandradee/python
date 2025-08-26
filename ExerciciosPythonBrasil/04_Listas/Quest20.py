'''
20 - As Organizações Tabajara resolveram dar um abono aos seus colaboradores
em reconhecimento ao bom resultado alcançado durante o ano que passou.
Para isto contratou você para desenvolver a aplicação que servirá como uma
projeção de quanto será gasto com o pagamento deste abono.
Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os
representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:
a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de
dezembro; a.O piso do abono será de 100 reais, isto é, aqueles funcionários
cujo salário for muito baixo, recebem este valor mínimo; Neste momento,
não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos,
impostos ou outras particularidades. Seu programa deverá permitir a digitação do salário
de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero)
encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor
do abono concedido a cada colaborador, de acordo com a regra definida acima.
Ao final, o programa deverá apresentar:
'''

salarios = []
abonos = []
quantidadeFuncionarios = 0
abonosMinimos = 0
maiorAbono = 0

while True:
    
    salario = float(input("Informe o salário do colaborador: "))
    
    if(salario == 0):
        break
    
    salarios.append(salario)
    quantidadeFuncionarios += 1
    
for i in range(len(salarios)):
    if(salarios[i]) < 500:
        abono = 100;
        abonosMinimos += 1
    else:
        abono = salarios[i] * 0.20
    abonos.append(abono)
    
for i in abonos:
    if(i > maiorAbono):
        maiorAbono = i

print("-" * 50)
print(f"Total de colaboradores: {quantidadeFuncionarios}")
print(f'Total gasto com abonos: R${sum(abonos)}')
print(f'Quantidade de valor mínimo pago: {abonosMinimos}')
print(f'Maior valor de abono pago: R${maiorAbono}')
