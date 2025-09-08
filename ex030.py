numero = int(input(f'{'\033[35m'}Me diga um número qualquer: {'\033[m'}'))
if numero % 2 == 0:
    print(f'O número {numero} é {'\033[34m'}PAR{'\033[m'}')
else:
    print(f'O número {numero} é {'\033[34m'}ÍMPAR{'\033[m'}')