largura = float(input('Largura da parede: '))
altura = float(input(f'Altura da parede: '))
area = largura * altura
print(f'Sua parede tem a dimensão de {largura} x {altura} e sua área é de {area:.2f}m²')
print(f'Para pintar essa parede, você precisará de {(area / 2):.2f}L de tinta')