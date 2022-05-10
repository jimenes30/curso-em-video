# Funções para sortear e somar
from random import randint

num = []


def sorteia():
    print(f'Sorteando 5 valores da lista: ', end=' ')
    for i in range(0, 5):
        num.append(randint(0, 9))
        print(f'\033[{randint(30, 37)}m{num[i]}\033[m', end=' ')
    print(f'PRONTO!')


def soma_par(listagem):
    pares = 0
    for c in range(0, len(listagem)):
        if listagem[c] % 2 == 0:
            pares += listagem[c]
    print(f'Somando os números pares de {listagem}, temos {pares}')


sorteia()
soma_par(num)
