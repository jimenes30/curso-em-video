# Interactive Helping System in Python


def titulo(msg):
    print(f'\033[43;1m~' * (len(msg) + 4))
    print(f'  {msg}')
    print(f'~' * (len(msg) + 4))


def ajuda():
    from time import sleep
    while True:
        r = str(input("\033[mFunção ou Biblioteca > "))
        if r.upper() == "FIM":
            break
        print(f'\033[42;7m~' * 40)
        print(f'   Acessando o manual do comando \'{r}\'')
        print(f'~' * 40)
        sleep(1)
        print(f'\033[40;7m')
        help(r)


# Programa principal
titulo("SISTEMA DE AJUDA")
ajuda()
