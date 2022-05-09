# Dissecando uma variável
algo = input('Digite algo: ')
print('O tipo primitivo desse algo é {}'.format(type(algo)))
if algo.isspace() == True:
    print('Só tem espaços ? \033[34m{}\033[m'.format(algo.isspace()))
print('É um número ? {}'.format(algo.isnumeric()))
print('É alfabético ? {}'.format(algo.isalpha()))
print('É alfanumérico ? {}'.format(algo.isalnum()))
print('Está em MAIÚSCULAS ? {}'.format(algo.isupper()))
print('Está em minúsculas ? {}'.format(algo.islower()))
print('Está Capitalizada ? {}'.format(algo.istitle()))
