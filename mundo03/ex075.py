# Análise de pessoas em uma Tupla
print(f'{" Análise de pessoas em uma Tupla ":☼^50}\n')
números = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print(f'O valor 9 apareceu {números.count(9)} vezes')
if números.count(3) != 0:
    print(f'O valor 3 foi digitado na {números.index(3) + 1}ª posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram: ', end='')
for c in range(0, 4):
    if números[c] % 2 != 1 and números[c] != 0:
        print(f'{números[c]}', end=' ')
print('\nFim do programa')
