# Maior e menor da sequência
pesado = 0
leve = 0
for i in range(1, 6):
    peso = float(input('Digite o peso da {}° Pessoa: '.format(i)))
    if i == 1:
        leve = peso
        pesado = peso
    if peso > pesado:
        pesado = peso
    if peso < leve:
        leve = peso
print('O maior peso foi {}kg e o menor foi {}kg'.format(pesado, leve))
