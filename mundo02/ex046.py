# Contagem Regressiva
from time import sleep
import pygame
from random import randint
from emoji import emojize as emoji

pygame.mixer.init()
pygame.init()
cor = ('\033[30m', '\033[31m', '\033[32m', '\033[33m',
       '\033[34m', '\033[35m', '\033[36m', '\033[37m', '\033[m')
emojis = {':fireworks:', ':sparkler:'}
print('{}{:~^33}{}'.format(cor[8], " FOGOS DE ARTIFÍCIO ", cor[8]))
opção = True
input('\n       \033[3m(Pressione ENTER )\033[m\n')
while opção:
    pygame.mixer.music.load('clock-tick-1s.mp3')
    for r in range(10, 0, -1):
        print('\n{}{:^33}{}\n'.format(cor[7], r, cor[7]))
        pygame.mixer.music.play()
        sleep(1)
    pygame.mixer.music.unload()
    pygame.mixer.music.load('fogos-de-artificio-2.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == 1:
        i = randint(0, 6)
        print('{0}{1}{2} {3}{4}'.format
              (cor[i], emoji(':sparkler:', True), cor[i + 1], emoji(':fireworks:', True), cor[i]), end=' ')
        sleep(1)
        continue
    opção = bool(input('\n\033[m[ ENTER ] SAIR\n[ 0 ] TENTAR DENOVO\n'))
print('FIM do programa')
