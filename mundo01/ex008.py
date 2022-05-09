# Conversor de medidas
n = float(input('Digite uma distância em metros: '))
print('A medida de {}m corresponde a: '.format(n))
print('{}km'.format(n / 1000))
print('{}hm'.format(n / 100))
print('{}dam'.format(n / 10))
print('{:.0f}dm'.format(n * 10))
print('{:.0f}cm'.format(n * 100))
print('{:.0f}mm'.format(n * 1000))
