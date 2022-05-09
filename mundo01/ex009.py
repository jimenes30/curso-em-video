# Tabuada
n = int(input('Digite um numero para ver sua tabuada: '))
print('.' * 16)
for i in range(1, 11):
    print('| {:>2} x {:<2} = {:>3}|'.format(i, n, (i * n)))
print('.' * 16)