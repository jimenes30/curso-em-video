# Catetos e hipotenusa
from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
# hip = (co ** 2 + ca ** 2) ** (1/2)
hip = hypot(co, ca)
print('O triângulo retângulo que possui cateto oposto {} e cateto adjacente {}. '
      'Possui como hipotenusa o valor {}.'.format(co, ca, hip))
