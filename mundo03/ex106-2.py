# Treino
cores = ("\033[m",  # 0 Sem COR
         "\033[31m",  # 1 Vermelho
         "\033[32m",  # 2 Verde
         "\033[33m",  # 3 Amarelo
         "\033[34m",  # 4 Azul
         "\033[35m",  # 5 Roxo
         "\033[36m",  # 6 Ciano
         "\033[37m",  # 7 Cinza
         "\033[7m",   # 8 Inverter
         "\033[1m"    # 9 Negrito
         )


def ajuda(comando):
    from time import sleep
    titulo(f'Acessando o Manual do Comando \'{comando}\'', cor=3, inverte=True, negrito=True)
    sleep(1)
    print(f'{cores[8]}', end="")
    help(comando)
    print(f'{cores[0]}', end="")


def titulo(msg, cor=0, inverte=False, negrito=False):
    tam = len(msg)
    if inverte:
        print(f'{cores[8]}', end='')
    if negrito:
        print(f'{cores[9]}', end='')
    print(f'{cores[cor]}', end='')
    print(f'-' * (tam + 4))
    print(f'  {msg}')
    print(f'-' * (tam + 4))
    print(f'{cores[0]}', end='')


while True:
    titulo(f'SISTEMA DE AJUDA PYHELP', cor=2, inverte=True, negrito=True)
    r = str(input('Função ou Biblioteca > ')).strip()
    if r.upper() == "FIM":
        break
    ajuda(r)
print('\n' * 4)
titulo(f'ATÉ LOGO', cor=6, inverte=True, negrito=True)
print('\n' * 2)
