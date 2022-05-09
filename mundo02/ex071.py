# Simulador de caixa eletrônico
""" minha solução
from time import sleep
print('=' * 50)
print(f'{" BANCO CHEV ":^50}')
print('=' * 50)
while True:
    valor = int(input('Qual valor a ser sacado ? R$ '))
    print('Total de: ', end='')

    # valores inválidos
    if valor == 0 or valor < 0:
        print('R$ 00,00')
        print('Finalizando...')
        sleep(1)
        break
    # notas de R$ 50,00
    notas_50 = valor // 50
    if notas_50 != 0:
        print(f'\n{notas_50} Cédulas de R$ {50:.2f}')
    valor -= notas_50 * 50  # resto

    # notas de R$ 20,00
    notas_20 = valor // 20
    if notas_20 != 0:
        print(f'{notas_20} Cédulas de R$ {20:.2f}')
    valor -= notas_20 * 20  # resto

    # notas de R$ 10,00
    notas_10 = valor // 10
    if notas_10 != 0:
        print(f'{notas_10} Cédulas de R$ {10:.2f}')
    valor -= notas_10 * 10  # resto

    # notas de R$ 1,00
    notas_1 = valor // 1
    if notas_1 != 0:
        print(f'{valor} Moedas de R$ {1:.2f}')
    print('=' * 50)
    while True:
        aluno = str(input('Nova operação ? [S/N] ')).strip().upper()
        if aluno != 'S' and aluno != 'N':
            print('Opção inválida. Tente novamente.')
        else:
            break
    if aluno == 'S':
        print('Processando ...')
        sleep(1)
    elif aluno == 'N':
        break

print('Volte sempre ao Banco CEV! Tenha um Bom dia!')
"""
from time import sleep
print('=' * 50)
print(f'{" BANCO CEV ":^50}')
print('=' * 50)
while True:
    valor = int(input('Qual valor a ser sacado ? R$ '))
    escolha = '0'
    total = valor
    tot_céd = 0
    céd = 50
    while True:
        if total >= céd:
            total -= céd
            tot_céd += 1
        else:
            if tot_céd != 0:
                print(f'total de {tot_céd} cédulas de R$ {céd}')
            tot_céd = 0
            if céd == 50:
                céd = 20
            elif céd == 20:
                céd = 10
            elif céd == 10:
                céd = 1
            else:
                break
    while escolha not in 'SN':
        escolha = str(input('Deseja sacar novamente ? [S/N] ')).strip().upper()[0]
        print('-' * 40)
    if escolha == 'N':
        break
print('Processando...')
sleep(1)
print('-=' * 25)
print('Volte sempre ao Banco CEV! Tenha um Bom dia!')
print('-=' * 25)
