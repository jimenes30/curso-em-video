# Separando dígitos de um número
"""
Método 1
numero = int(input('Informe um numero: '))
unidade = numero % 10 // 1
dezena = numero % 100 // 10
centena = numero % 1000 // 100
unidade_de_milhar = numero % 10000 // 1000
print('Analisando o número {}'.format(numero))
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(unidade_de_milhar))
"""
numero = int(input('Informe um número: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Analisando o número {}'.format(numero))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
