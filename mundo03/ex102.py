# Função para fatorial


def fatorial(num, show=False):
    """
    --> Função que calcula o fatorial de um número
    :param num: número a qual será calculado o fatorial
    :param show: mostra a conta (opcional)
    :return: retorna o fatorial de num
    Dev: Alfredo exercício CuroemVídeo
    """
    print(f"-" * 30)
    f = 1
    for i in range(num, 0, -1):
        f *= i
        if show:
            if i > 1:
                print(f'{i} x ', end='')
            else:
                print(f'1 = ', end='')
    return f


print(fatorial(5, show=True))
print(fatorial(5, show=False))
print(fatorial(5))
print(fatorial(5, True))
help(fatorial)
