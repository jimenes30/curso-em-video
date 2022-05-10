# treino
listagem = ("Lápis", 1,
            "Borracha", 1.50,
            "Caderno", 14.90,
            "Resma", 18,
            "Caneta Preta", 2,
            "Régua", 4,
            "Mochila", 50)
print("-" * 50)
print(f'{"MATERIAL ESCOLAR":^50}')
print("-" * 50)
for i in range(0, len(listagem)):
    if i % 2 == 0:
        print(f'{listagem[i]:.<40}', end='')
    else:
        print(f'R${listagem[i]:>7.2f}')
print("-" * 50)
