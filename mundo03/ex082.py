# Dividindo valores em várias listas
lista = []
pares = []
impares = []
while True:
    lista.append(int(input("Digite um valor: ")))
    r = str(input("Quer continuar? [S/N] "))
    if r in "Nn":
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'Você digitou os números {lista}')
print(f'Os números pares que você digitou: {pares}')
print(f'Números Ímpares que você digitou: {impares}')






"""
temp = []
par = []
impar = []
while True:
    p = int(input("Digite um número: "))
    if p in temp:
        pass
    else:
        temp.append(p)
        if p % 2 == 0:
            par.append(p)
        else:
            impar.append(p)
    r = str(input("Quer continuar ? [S/N]"))
    if r in "Nn":
        break
print('-=' * 30)
print(f'Você digitou os números {temp}')
if len(par) > 0:
    print(f'Os números Pares que você digitou: {par}')
else:
    print(f'Você não digitou nenhum número Par!')
if len(impar) > 0:
    print(f'Números ímpares que você digitou: {impar}')
else:
    print(f'Você não digitou nenhum número Ímpar!')
"""
