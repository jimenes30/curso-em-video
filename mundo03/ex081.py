# Extraindo pessoas de uma temp
lista = []
while True:
    n = int(input("Digite um número: "))
    lista.append(n)
    r = str(input("Deseja continuar ? [S/N]"))
    if r in "Nn":
        break
print(f'Você digitou \033[31m{len(lista)}\033[m números')
print(f'Você digitou os números {sorted(lista, reverse=True)}')
if 5 in lista is True:
    print(f'O valor 5 \033[31mNÃO\033[m foi digitado')
else:
    print(f'\033[34mO valor \033[m5\033[34m foi digitado\033[m')
