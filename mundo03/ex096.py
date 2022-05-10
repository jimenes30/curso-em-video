# Função que calcula área
def area(l, c):
    terreno = l * c
    print(f'A área de um terreno {l} x {c} é de {terreno:.2f}m²')


def lin(msg):
    print('\033[34m-\033[m' * len(msg)*2)
    print(f'{msg:^{len(msg)*2}}')
    print('\033[33m-\033[m' * len(msg)*2)


# Programa principal
lin('Controle de Terrenos')
area(float(input("Largura(m): ")), float(input("Comprimento(m): ")))
lin('FIM')
