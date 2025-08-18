from random import shuffle
'''
lista = []
for i in range(1,5):
    lista.append(input(f'{i}º Aluno: '))

ordem = random.sample(range(0,4), 4)
print(f'A ordem de apresetação será: ')
for i in range(0,4):
    print(f'{i+1}º {lista[ordem[i]]}')
'''
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
print('A ordem de apresentação será ')
shuffle(lista)
print(lista)
