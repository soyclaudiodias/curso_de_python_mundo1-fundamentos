medida = float(input('Uma distância em metros: '))
# print(f'A medida de {medida}m corresponde a {(medida*100):.0f}cm e {(medida*1000):.0f}mm')
print(f'A medida de {medida}m corresponde a:')
print(f'{medida/1000}km\n{medida/100}hm\n{medida/10}dam\n{(medida*10):.0f}dm\n{(medida*100):.0f}cm\n{(medida*1000):.0f}mm')