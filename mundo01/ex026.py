# Primeira e última ocorrência de uma string
frase = str(input('Digite uma frase:\n')).strip().lower()
fatia = frase.split()
print('A letra A aparece {} vezes na frase.'.format(frase.count('a')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('a') + 1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('a') + 1))
