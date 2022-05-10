# Mais sobre Matriz em Python
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
mai2l = []
soma3c = par = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}][{c}]: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        if c == 2:
            soma3c += matriz[l][c]
        if l == 1:
            mai2l.append(matriz[l][c])
print("-" * 60)
for l in range(0, 3):
    for c in range(0, 3):
        if c == 0:
            print(f'{" ":<17}', end='')
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print("-" * 60)
print(f'A soma dos valores pares é {par}.')
print(f'A soma dos valores da terceira coluna é {soma3c}.')
print(f'O maior valor da segunda linha é {sorted(mai2l)[2]}.')

