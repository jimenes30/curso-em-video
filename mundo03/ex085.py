# Listas com pares e ímpares
lista = [[], []]
for c in range(1, 8):
    temp = int(input(f'Digite o {c}° número: '))
    if temp % 2 == 0:
        lista[0].append(temp)
    else:
        lista[1].append(temp)
lista[0].sort()
lista[1].sort()
print(f'Você digitou os números {lista}')
print(f'Os números pares são: {lista[0]}')
print(f'Os números ímpares foram: {lista[1]}')
