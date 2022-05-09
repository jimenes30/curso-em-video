# Maior e menor
""" Método 'burro'
a = int(input('Primeiro valor:\n'))
b = int(input('Segundo valor:\n'))
c = int(input('Terceiro valor:\n'))
if a > b > c:
    maior = a
    menor = c
if a > c > b:
    maior = a
    menor = b
if b > c > a:
    maior = b
    menor = a
if b > a > c:
    maior = b
    menor = c
if c > b > a:
    maior = c
    menor = a
if c > a > b:
    maior = c
    menor = b
print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))
"""
a = int(input('Primeiro valor:\n'))
b = int(input('Segundo valor:\n'))
c = int(input('Terceiro valor:\n'))
# Testando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Testando quem é maior
maior = c
if b > c and b > a:
    maior = b
if a > c and a > b:
    maior = a
print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))
