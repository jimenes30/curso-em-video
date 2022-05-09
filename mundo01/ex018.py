# Seno, Cosseno e Tangente
from math import radians, sin, cos
angulo = float(input('Digite o valor do ângulo para saber o seno, cosseno e a tangente: '))
x = radians(angulo)
seno = sin(x)
cosseno = cos(x)
tangente = seno / cosseno
print('.\nO ângulo de {}°, possui:\nSeno = {:.2f}\nCosseno = {:.2f}\n'
      'Tangente = {:.2f}\n.'.format(angulo, seno, cosseno, tangente))
