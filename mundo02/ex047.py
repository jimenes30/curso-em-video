# Contagem de pares/ímpares
from time import sleep
opção = '1'
while opção == '1':
    contador = 0
    inicio = int(input('Digite um número inicial: '))
    fim = int(input('Digite até que número contar: '))
    if inicio % 2 == 0:
        print('\033[34m{:-^50}\033[m'.format(' Contagem de Pares '))
        for i in range(inicio, fim + 1, 2):
            contador += 1
            print('{:>2}° - {:>2}'.format(contador, i))
            sleep(0.5)
    else:
        print('\033[31m{:-^50}\033[m'.format(' Contagem de Ímpares '))
        for i in range(inicio, fim + 1, 2):
            contador += 1
            print('{:>2}° - {:>2}'.format(contador, i))
            sleep(0.5)
    opção = str(input('Deseja continuar ?\n[ 0 ] NÃO\n[ 1 ] SIM\n'))
print('FIM')
