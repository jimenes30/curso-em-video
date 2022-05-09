# GAME: Pedra, Papel e Tesoura
from time import sleep
from random import randint
print('\033[7;1;37m-~\033[m' * 30)
print('\033[7;1;37m{:^60}\033[m'.format(' GAME: JOKENPÔ ! '))
print('\033[7;1;37m~-\033[m' * 30)
print('Suas opções:\n[ 1 ] Pedra\n[ 2 ] Papel\n[ 3 ] Tesoura')
jogador = int(input('Qual é a sua jogada ? '))
cpu = randint(1, 3)
# itens = ('nulo', 'Pedra', 'Papel', 'Tesoura')
if jogador == 1:
    jogador = 'Pedra'
elif jogador == 2:
    jogador = 'Papel'
elif jogador == 3:
    jogador = 'Tesoura'
if cpu == 1:
    cpu = 'Pedra'
elif cpu == 2:
    cpu = 'Papel'
elif cpu == 3:
    cpu = 'Tesoura'
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=-' * 10)
print('\033[1;35mComputador\033[m jogou {}\n\033[3mVocê\033[m jogou {}'.format(cpu, jogador))
print('-=-' * 10)
if jogador == cpu:
    print('\033[30mEMPATE\033[m')
elif jogador == 'Pedra' and cpu == 'Papel':
    print('\033[1;35mComputador\033[m Venceu')
elif jogador == 'Pedra' and cpu == 'Tesoura':
    print('\033[34;3mJogador\033[m Venceu')
elif jogador == 'Papel' and cpu == 'Pedra':
    print('\033[34;3mJogador\033[m Venceu')
elif jogador == 'Papel' and cpu == 'Tesoura':
    print('\033[1;35mComputador\033[m Venceu')
elif jogador == 'Tesoura' and cpu == 'Papel':
    print('\033[34;3mJogador\033[m Venceu')
elif jogador == 'Tesoura' and cpu == 'Pedra':
    print('\033[1;35mComputador\033[m Venceu')
