# Detector de Palíndromos
from random import randint
from random import shuffle
print('\033[1m{:=^50}\033[m'.format(' Detector de Palíndromos '))
frase = str(input('Digite uma frase: ')).strip().upper()
# frases = ['apos a sopa', 'a sacada da casa', 'anotaram a data da maratona', 'a torre da derrota', 'o lobo ama o bolo']
# shuffle(frases)
# palavra = randint(0, 4)
# frase = frases[palavra]
fatiado = frase.split()
junto = ''.join(fatiado)
print('{}, de trás pra frente fica {}.'.format(junto, junto[::-1]))
if junto == junto[::-1]:
    print('A frase pode ser classificada como \033[33mPALÍNDROMO\033[m!')
else:
    print('A frase \033[1;31mNÃO\033[m É UM \033[33mPALÍNDROMO\033[m !!!')
