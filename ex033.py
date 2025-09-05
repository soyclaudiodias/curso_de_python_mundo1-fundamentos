n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
maior = max(n1, n2, n3)
menor = min(n1, n2, n3)
'''
if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3

if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n2 > n2:
    maior = n3
'''
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')