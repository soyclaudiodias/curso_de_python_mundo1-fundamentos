from random import choice
'''
lista = []
for i in range(1,5):
    lista.append(input(f'{i}º Aluno: '))
'''
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
print(f'O aluno escolhido foi {choice(lista)}')
