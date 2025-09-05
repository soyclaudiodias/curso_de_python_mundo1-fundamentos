salario = float(input('Qual é o salário de funcionário? R$'))
if salario > 1250.00:
    novo_salario = salario * 1.1
else:
    novo_salario = salario * 1.15
print(f'Quem ganhava R${salario:.2f} passa a ganhar R${(novo_salario):.2f} agora.')