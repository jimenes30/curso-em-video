# Progressão aritmética v2.0
print('{:~^50}'.format(' Progressão Aritmética v2.0 '))
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
contador = 0
termo = a1
while contador != 10:
    contador += 1
    #termo = a1 + (contador - 1) * razão
    print('{:>2}° Termo = {:>2}'.format(contador, termo))
    termo += r
