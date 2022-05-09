# Jogo da advinhação
from time import sleep
from random import randint
print('\033[33m-=-\033[m' * 20)
print('\033[34mVou pensar em um número entre 0 e 5. Tente advinhar...\033[m')
print('\033[33m-=-\033[m' * 20)
palpite_cpu = randint(0, 5)
palpite_usuario = int(input('Em que número eu pensei ?\n'))
print('\033[37mPROCESSANDO...\033[m')
sleep(2)
if palpite_usuario == palpite_cpu:
    print('\033[32mPARABÉNS! Você conseguiu me vencer!\033[m')
else:
    print('\033[31mGANHEI! Eu pensei no número {} e não no {}\033[m'.format(palpite_cpu, palpite_usuario))
