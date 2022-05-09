# Cálculo do fatorial

# Fazer com FOR

"""
import math
print('{:-^50}'.format(' Cálculo de fatorial '))
num = int(input('Digite um número: '))
print('O fatorial de {} é igual a {}'.format(num, math.factorial(num)))
palavra = num
print('{}! ='.format(num), end=' ')
while palavra != 1:
    print('{} x'.format(palavra), end=' ')
    palavra = palavra - 1
print('1 = {}'.format(math.factorial(num)))
"""
print('{:-^50}'.format(' Cálculo de fatorial '))
num = int(input('Digite um número para saber seu fatorial: '))
contador = num
acumulado = 1
print('5! = ', end='')
while contador > 0:
    acumulado = acumulado * contador
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    contador -= 1

print('{}'.format(acumulado))
