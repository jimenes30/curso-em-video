# Aprimorando os dicionários
time = []
while True:
    jogador = {"nome": str(input("Nome do jogador: "))}
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou ? '))
    gols = []
    for c in range(1, partidas + 1):
        gols.append(int(input(f'    Quantos gols na partida {c} ? ')))
    jogador["gols"] = gols
    jogador["total"] = sum(gols)
    time.append(jogador.copy())
    while True:
        continua = str(input("Quer continuar? [S/N] ")).upper()[0]
        if continua in "SN":
            break
        print(f'ERRO! Digite somente S ou N.')
    if continua == "N":
        break
print(f'-=' * 30)
print(f'-' * 60)
print(f'{"cod":<4}{"nome":<15}{"gols":<15}{"total":^15}')
for c, j in enumerate(time):
    print(f'{c+1:<4}{j["nome"]:<15}{str(j["gols"]):<15}{j["total"]:^15}')
print(f'-' * 60)
print(f'-=' * 30)
while True:
    escolha = int(input("Mostrar dados de qual jogador? [999 encerra] "))
    if escolha == 999:
        break
    if escolha > len(time) or escolha <= 0:
        print(f'ERRO! não existe jogador com código {escolha}')
    else:
        print(f' -- Levantamento do jogador {time[escolha-1]["nome"]}:')
        for p, v in enumerate(time[escolha-1]["gols"]):
            print(f'        --> No jogo {p+1} fez {v} gols.')
print(f'\n{"> Volte Sempre! <":^50}')
