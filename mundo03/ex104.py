# Validando entrada de dados em Python


def leiaint(msg):
    print(f'-' * 30)
    while True:
        num = str(input(f'{msg}')).strip()
        if num.isnumeric():
            num = int(num)
            break
        else:
            print(f'\033[31mERRO! Digite um número inteiro válido.\033[m')
    return num


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
