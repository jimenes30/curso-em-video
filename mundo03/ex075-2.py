# treino
tup = (int(input('Digite um número: ')), int(input('Digite um número: ')),
       int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'O valor 9 apareceu {tup.count(9)} vezes')
if tup.count(3) != 0:
    print(f'O valor 3 foi digitado na posição {tup.index(3) + 1}')
else:
    print(f'O número 3 não foi digitado')
print(f'Os números pares digitados foram: ', end='')
for i in range(0, 4):
    if tup[i] % 2 == 0:
        print(f'{tup[i]} ', end='')
