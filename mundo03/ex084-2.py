# Lista composta e análise de pessoas
temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input("Nome: ")))
    temp.append(float(input("Peso: ")))
    princ.append(temp[:])
    if len(princ) == 1:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        elif temp[1] < menor:
            menor = temp[1]
    temp.clear()
    r = str(input("Quer continuar? [S/N] "))
    if r in "Nn":
        break
print('-=' * 30)
print(f'Foram cadastradas {len(princ)} pessoas')
print(f'O maior peso foi {maior}Kg. E os gordos são: ', end='')
for p in princ:
    if p[1] == maior:
        print(f' [{p[0]}]', end=' ')
print(f'\nO menor peso foi {menor}Kg. E os magros são: ', end='')
for p in princ:
    if p[1] == menor:
        print(f' [{p[0]}]', end='')
print('\n')
print('-=' * 30)
