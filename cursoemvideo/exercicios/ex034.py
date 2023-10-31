salario = float(input('Qual é o salário do funcionário? R$'))
novo = salario + (salario * 15/100) if salario <= 1250 else salario + (salario * 10/100)
print(f'Quem ganhava R${salario:.2f} passa a ganhar R${novo:.2f} agora.')