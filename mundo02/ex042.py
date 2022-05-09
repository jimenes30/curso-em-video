# Analisando Triângulos v2.0
print('\033[30m-\033[m\033[34m=\033[m' * 20)
print('{:^40}'.format('Analisador de Triângulos v2.0'))
print('\033[30m-\033[m\033[34m=\033[m' * 20)
a = float(input('Primeiro segmento:\n'))
b = float(input('Segundo segmento:\n'))
c = float(input('Terceiro segmento:\n'))
if a < (b + c) and b < (a + c) and c < (a + b):
    print('Os segmentos acima PODEM FORMAR um TRIÂNGULO', end=' ')
    if a != b != c != a:
        print('ESCALENO')
    elif a == b != c or a == c != b or c == b != a:
        print('ISÓSCELES')
    elif a == b == c:
        print('EQUILÁTERO')
else:
    print('Os segmentos acima NÃO PODEM formar um TRIÂNGULO')
