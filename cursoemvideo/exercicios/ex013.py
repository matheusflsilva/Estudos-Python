salario = float(input('Qual é o salário do Funcionário? R$'))
print(f'Um funcionário que ganhava R${salario:.2f}, com 15% de aumento, passa a receber R${salario + (salario * 15/100):.2f}')
