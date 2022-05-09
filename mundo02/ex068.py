# Jogo do Par ou Ímpar
from random import randint
print('=-' * 25)
print(f'{" Jogo do PAR ou ÍMPAR ":-^50}')
print('=-' * 25)
placar = 0
while True:
    jogador_jogada = ' '
    computador_jogada = 'I'
    jogador_número = int(input('Digite um valor: '))
    computador_número = randint(0, jogador_número + 3)
    while jogador_jogada not in 'PI':
        jogador_jogada = str(input('PAR ou IMPAR ? [P/I] ')).strip().upper()[0]
    soma = computador_número + jogador_número
    if jogador_jogada == 'I':
        computador_jogada = 'P'
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    print(f'Você jogou {jogador_número} e o computador jogou {computador_número}.')
    print(f'Total de {soma} deu {resultado}!')
    print('-' * 40)
    if resultado[0] != jogador_jogada:
        print('Você Perdeu!')
        break
    else:
        print('Você Ganhou!')
        print('Vamos jogar novamente...')
        print('=' * 40)
    placar += 1
print('-=' * 20)
print(f'Fim do jogo. Vitórias consecutivas: {placar}')
print('=-' * 20)
