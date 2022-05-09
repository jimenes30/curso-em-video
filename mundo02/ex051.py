# Progressão Aritmética
print('\033[7;1m{:-^50}\033[m'.format('10 primeiros termos de uma Progressão Aritmética'))
a1 = int(input('Digite o primeiro termo da progressão: '))
r = int(input('Digite a razão: '))
for c in range(1, 11):
    t = a1 + r * (c - 1)
    print('|\033[31m{:>2}\033[m° Termo == \033[1m{:>2}\033[m|'.format(c, t))
