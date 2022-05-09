# Tabuada v2.0
print('\033[3;1m{:-^38}\033[m'.format(' Tabuada v2.0 '))
numero = int(input('Digite um número para ver sua tabuada: '))
for i in range(1, 11):
    print('\033[7m|\033[m {:>2} \033[30mx\33[m {:>2} = {:>2} \033[7m|\033[m'.format(i, numero, numero * i))
