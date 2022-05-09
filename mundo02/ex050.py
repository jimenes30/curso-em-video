# Soma dos pares
soma = 0
print('\033[1m{:_^50}\033[m'.format('Soma de Números Pares'))
for c in range(1, 7):
    numero = int(input('Digite um número inteiro: '))
    if numero % 2 == 0:
        soma += numero
print('A soma dos números pares acima é {}.'.format(soma))
