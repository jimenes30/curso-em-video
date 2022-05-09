# Números Primos
"""
print('{:~^50}'.format('ANALISADOR DE PRIMOS'))
número = int(input('Digite um número: '))
soma = 0
for palavra in range(1, número + 1):
    if número % palavra == 0:
        soma += 1
if soma == 2:
    print('O número \033[34m{}\033[m É um número \033[32mPRIMO\033[m'.format(número))
else:
    print('O número {} \033[1;31mNÃO\033[m é \033[33mPRIMO\033[m'.format(número))
"""
from time import sleep
cor = ['\033[30m', '\033[31m', '\033[32;1m', '\033[33m', '\033[3;1m', '\033[m']
print('=' * 40)
print('{:^40}'.format('ANALISADOR DE PRIMOS'))
print('=' * 40)
número = int(input('Digite um número: '))
divisores = 0
for i in range(1, número + 1):
    if número % i == 0:
        print('\033[33m', end='')
        divisores += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(i), end=' ')
    sleep(0.5)
if divisores == 2:
    print('\n\033[mO número {}{}{} é {}divisível somente por 1 e por ele mesmo{}.\n'
          'Logo é um número {}PRIMO!{}'.format(cor[0], número, cor[-1], cor[4], cor[-1], cor[3], cor[-1]))
else:
    print('\n\033[mO número {}{}{} tem {}{}{} divisores exatos.\n'
          'Logo, {}NÃO{} É PRIMO!'.format(cor[0], número, cor[-1], cor[0], divisores, cor[-1], cor[1], cor[-1]))
