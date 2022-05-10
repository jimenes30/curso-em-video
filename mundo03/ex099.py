# Função que descobre o Maior
from random import randint
from time import sleep


def maior(*valores):
    print(f'\033[32m-=\033[m' * 30)
    cont_maior = 0
    print(f'Analisando os valores passados ...')
    for c in range(0, len(valores)):
        print(f'\033[{randint(30, 37)}m{valores[c]}\033[m', end=' ')
        sleep(0.95)
        if valores[c] > cont_maior:
            cont_maior = valores[c]
    print(f'Foram informados {len(valores)} valores ao todo.')
    sleep(1)
    print(f'O maior valor foi \033[{randint(30, 37)}m{cont_maior}\033[m')
    sleep(0.5)


maior(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
maior(randint(0, 9), randint(0, 9), randint(0, 9))
maior(randint(0, 9), randint(0, 9))
maior(randint(0, 9))
maior()
