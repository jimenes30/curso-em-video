# Lista de Preços com Tuplas
listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90,
            'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
print(f'{"-"}' * 60)
print(f'{"LISTAGEM DE PREÇOS":^60}')
print(f'{"-"}' * 60)
for c in range(0, len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<50}', end='')
    else:
        print(f'R$ {listagem[c]:>6.2f}')
print(f'{"":-<60}')
