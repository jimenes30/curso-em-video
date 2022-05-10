# treino
from random import randint
tup = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os números sorteados foram: {tup[::]}')
print(f'O maior valor foi: {max(tup)}')
print(f'O menor valor foi: {min(tup)}')
