# Super Progressão Aritmética v3.0
print('{:-^50}'.format(' Progressão Aritmética v3.0 '))
a1 = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
contador = n = 0
limite = 10
termo = a1
while contador != limite:
    contador += 1
    n += 1
    # termo = a1 + (p - 1) * razão
    print('{:>2}° Termo = {:>2}'.format(n, termo))
    termo += razão
    if contador == limite:
        contador = 0
        limite = int(input('Deseja mostrar mais quantos termos ?\n[ 0 ] Para não mostrar mais nenhum\n'))
        if limite == 0:
            limite = contador
print('Progressão finalizada com {} Termos mostrados'.format(n))
