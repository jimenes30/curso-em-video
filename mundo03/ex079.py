# Valores únicos em uma temp
numeros = list()
while True:
    n = int(input("digite um valor: "))
    if n not in numeros:
        numeros.append(n)
        print("Valor registrado com Sucesso!")
    else:
        print("Valor Duplicado, não vou adicionar !")
    r = str(input("quer continuar? [S/N]"))
    if r in "Nn":
        break
print("-="*30)
numeros.sort()
print(f'Você digitou os valores {numeros}')

"""
lista_num = []
c = 0
while True:
    lista_num.append(int(input('Digite um valor: ')))
    if lista_num.count(lista_num[-1]) > 1:
        lista_num.remove(lista_num[-1])
        print('Valor Duplicado! Não vou adicionar na temp !')
    elif lista_num.count(lista_num[-1]) == 1:
        print('Valor adicionado com sucesso !')
    while True:
        aluno = str(input('Deseja continuar ? [S/N] ')).strip().upper()
        if aluno == "S" or aluno == "N":
            break
        else:
            print('Tente novamente. ', end='')
    if aluno == 'S':
        pass
    elif aluno == 'N':
        break
print('-=' * 50)
print(f'Você digitou os números {sorted(lista_num)}')
print('-=' * 50)
print('FIM DO PROGRAMA')
"""