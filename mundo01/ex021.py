# Tocando um MP3
"""Método 1
import emoji
import playsound
print(emoji.emojize('Python é :snake:', use_aliases=True))
playsound.playsound('solving-secret-sound.mp3')"""
from pygame import mixer, init
from time import sleep
from math import ceil
mixer.init()
init()
mixer.music.load("mipha's-theme.mp3")
#input('Aperte Enter')
mixer.music.play()
while mixer.music.get_busy() == 1:
    print(' ' * 50 + f'\033[33m{(ceil(mixer.music.get_pos()) / 1000):.0f}s\033[m', end='\n' * 2)
    sleep(1)
