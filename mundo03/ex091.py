# Jogo de pessoas em Python
from random import randint
from time import sleep
from operator import itemgetter
classificacao = list()
jogadores = {"Jogador 1": randint(1, 6), "Jogador 2": randint(1, 6),
             "Jogador 3": randint(1, 6), "Jogador 4": randint(1, 6)}
print(f'Valores sorteados:')
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
classificacao = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print(f'{"== Ranking dos Jogadores ==":^60}')
for i, v in enumerate(classificacao):
    print(f'{i+1}° Lugar: {v[0]} com {v[1]}')
