# Lista composta e análise de pessoas
dados = []
nome_gordo = [""]
nome_magro = [""]
pesos = []
gordos = [0]
magros = [9999]
while True:
    dados.append(input("Nome: "))
    dados.append((float(input("Peso: "))))
    pesos.append(dados[1])
    if dados[1] > gordos[-1]:
        if dados[1] not in gordos:
            gordos.clear()
            nome_gordo.clear()
        gordos.append(dados[1])
        nome_gordo.append(dados[0])
    elif dados[1] == gordos[-1]:
        gordos.append(dados[1])
        nome_gordo.append(dados[0])
    if dados[1] < magros[-1]:
        if dados[1] not in magros:
            magros.clear()
            nome_magro.clear()
        magros.append(dados[1])
        nome_magro.append(dados[0])
    elif dados[1] == magros[-1]:
        magros.append(dados[1])
        nome_magro.append(dados[0])
    dados.clear()
    r = str(input("Quer continuar? [S/N] "))
    if r in "Nn":
        break
print(f'Foram cadastradas {len(pesos)} pessoas')
print(f'O maior peso foi {gordos[0]} e os gordos são:', end='')
for i in nome_gordo:
    print(f' {i}', end='')
print(f'\nO menor peso foi {magros[0]} e os magros são:', end='')
for i in nome_magro:
    print(f' {i}', end='')
