from math import radians, sin, cos, tan
angulo = float(input('Digite um ângulo que você deseja: '))
print(f'O ângulo de {angulo} tem o SENO de {sin(radians(angulo)):.2f}')
print(f'O ângulo de {angulo} tem o COSSENO de {cos(radians(angulo)):.2f}')
print(f'O ângulo de {angulo} tem a TANGENTE de {tan(radians(angulo)):.2f}')