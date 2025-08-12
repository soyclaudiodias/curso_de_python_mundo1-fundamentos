dias = int(input('Quantos dias alugador? '))
km = float(input('Quantos Km rodados? '))
print(f'O total a pagar é de R$ {((60 * dias) + (km * 0.15)):.2f}')