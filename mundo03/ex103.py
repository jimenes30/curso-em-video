# Ficha do Jogador


def ficha(nome_jogador="<desconhecido>", numero_gols="0"):
    print(f'-' * 30)
    n = str(input("Nome do Jogador: "))
    g = str(input("Número de gols: "))
    if len(g) > 0 and g.isnumeric() == True:
        numero_gols = g
    if len(n) > 0:
        nome_jogador = n
    print(f'O jogador {nome_jogador} fez {numero_gols} gol(s) no campeonato')


ficha()
