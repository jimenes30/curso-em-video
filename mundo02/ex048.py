# Soma Ímpares
from time import sleep
soma = 0
print('Soma dos números ímpares de 1 a 500')
sleep(2)
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
        print('{}\n'.format(i))
print('\nA soma dos números acima é {}.'.format(soma))
