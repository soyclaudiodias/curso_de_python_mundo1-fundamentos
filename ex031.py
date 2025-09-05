distancia = float(input('Qual é a distância de sua viagem? '))
print(f'Você está prestes a começar uma viagem de {distancia:.1f}Km.')
# preco = distancia * 0.5 if distancia <= 200 else distancia * 0.45
if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45
print(f'E o preço da sua passagem será de R${preco:.2f}')