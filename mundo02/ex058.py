# Jogo da advinhação v2.0
from random import randint
from time import sleep
import pyttsx3


def falar_texto(texto='Olá', rate=145, vol=1, idioma=0):
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', rate)  # Definindo ritmo de fala
    engine.setProperty('volume', vol)  # Define o volume entre 0(minimo) e 1(maximo)
    """Voz"""
    voices = engine.getProperty('voices')  # Pegando detalhes da voz atual
    engine.setProperty('voice', voices[idioma].id)  # Índice 0 para Br, 1 para Inglês[ambas femeas]
    # Texto que a engine vai falar #
    engine.say(texto)
    engine.runAndWait()
    engine.stop()


print('{:×^55}'.format('= Jogo da advinhação v2.0 ='))
print('Vou pensar em um número de 1 a 10. Tente advinhar ...')
falar_texto('Vou pensar em um número de 1 a 10. Tente advinhar ...', 200)
print('PROCESSANDO...')
falar_texto('Processando', rate=300)
for i in range(1, 4):
    print('•')
    sleep(1)
palpite_computador = randint(1, 10)
palpite_jogador = palpite_computador + 1
tentativas = 0
falar_texto('Pensei!', rate=300)
print('{}{}{}'.format('Pensei !\n', '-' * 30, '\n'))
while palpite_jogador != palpite_computador:
    palpite_jogador = int(input('Qual é seu palpite ?\n'))
    if palpite_jogador != palpite_computador:
        print('Errou [\033[31m×\033[m]\nTente novamente.')
        falar_texto('Errou! Tente novamente', rate=300)
        if palpite_jogador > palpite_computador:
            falar_texto('É menos!', rate=300)
            print('Menos... Tente mais uma vez')
        if palpite_jogador < palpite_computador:
            falar_texto('É MAIS', rate=300)
            print('Mais... Tente denovo')
        palpite_jogador = palpite_computador + 1
    tentativas += 1
    print('Tentativas: {}\n{}{}'.format(tentativas, '\n', '-' * 30))
print('Parabéns! você venceu !\nA máquina pensou no número {}'.format(palpite_computador))
falar_texto(f'Parabéns! você venceu !\nA máquina pensou no número {palpite_computador}', rate=300)
if tentativas == 1:
    print('Você é FERA ! Precisou de apenas {} palpite.'.format(tentativas))
    falar_texto(f'Você é FERA ! Precisou de apenas {tentativas} palpite.')
else:
    print('Você precisou dar {} palpites.'.format(tentativas))
    falar_texto(f'Você precisou dar {tentativas} palpites')
if tentativas == 1:
    print('Classificação: Grande Mestre da Advinhação')
    falar_texto('Classificação: Grande Mestre da Advinhação')
elif tentativas == 2:
    print('Classificação: Advinhador Mestre')
    falar_texto(f'Classificação: Advinhador Mestre')
elif tentativas == 3:
    print('Classificação: Advinhador Intermediário')
    falar_texto('Classificação: Advinhador Intermediário')
elif tentativas == 4:
    print('Classificação: Advinhador júnior')
    falar_texto('Classificação: Advinhador júnior')
elif tentativas == 5:
    print('Classificação: Advinhador esforçado')
    falar_texto('Classificação: Advinhador esforçado')
elif 10 >= tentativas >= 6:
    print('Classificação: Ruim')
    falar_texto('Classificação: Ruim')
elif tentativas == 11:
    print('Classificação: Azarado')
    falar_texto('Classificação: Azarado')
elif tentativas > 11:
    print('Classificação: Incapaz')
    falar_texto('Classificação: Incapaz')
falar_texto('Vou chamar minha assistente pra falar isso aqui', rate=300)
falar_texto('GAME OVER', idioma=1)
print(f'FIM DE JOGO\nGAME OVER!!!')
