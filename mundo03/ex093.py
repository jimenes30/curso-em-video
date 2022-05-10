# Cadastro de jogador de futebol
nome = str(input("Nome do jogador: "))
partidas = int(input(f'Quantas partidas {nome} jogou ? '))
gols = []
ficha = {}
for c in range(0, partidas):
    gols.append(int(input(f'    Quantos gols na partida {c} ? ')))
ficha["nome"] = nome
ficha["gols"] = gols
ficha["total"] = sum(gols)
print(f'-=' * 30)
print(ficha)
print(f'-=' * 30)
for k, v in ficha.items():
    print(f'O campo {k} tem o valor {v}')
print(f'-=' * 30)
print(f'O jogador {ficha["nome"]} jogou {partidas} partidas')
for p, v in enumerate(gols):
    print(f'    => Na partida {p}, fez {v} gols.')
print(f'E foi um total de {ficha["total"]} gols')
