from random import randint
from time import sleep
print(f'{'\033[33m'}-=-{'\033[m'}' * 20)
print(f'{'\033[34m'}Vou pensar em um número entre 0 e 5. Tente adivinhar...{'\033[m'}')
print(f'{'\033[33m'}-=-{'\033[m'}' * 20)
computador = randint(0, 5)
jogador = int(input('Em que número eu pensei? '))
print(f'{'\033[35m'}PROCESSANDO...{'\033[m'}')
sleep(3)
if jogador == computador:
    print(f'{'\033[32m'}PARABÉNS! Você conseguiu me vencer!{'\033[m'}')
else:
    print(f'{'\033[31m'}GANHEI! Eu pensei no número {computador} e não no {jogador}!{'\033[m'}')