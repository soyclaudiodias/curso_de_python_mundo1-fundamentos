from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
# print(f'A hipotenusa vai medir {math.sqrt(math.pow(co, 2) + math.pow(ca, 2)):.2f}')
print(f'A hipotenusa vai medir {hypot(co, ca):.2f}')