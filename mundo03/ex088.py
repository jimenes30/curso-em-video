# Palpites para a Mega Sena
from random import sample
from time import sleep
print(f'-' * 30)
print(f'{"JOGA NA MEGA SENA!":^30}')
print(f'-' * 30)
lista = []
temp = []
nums = []
for c in range(1, 61):
    nums.append(c)
njogos = int(input("Quantos jogos você quer que eu sorteie? "))
for c in range(0, njogos):
    temp.append(sample(nums, 6))
    lista.append(temp[0])
    temp.clear()
print(f'-=' * 4, f'SORTEANDO {njogos} JOGOS ', f'-=' * 4)
for i in range(0, njogos):
    print(f'Jogo {i+1}: {sorted(lista[i])}')
    sleep(1)
print(f'-=' * 5, f'{"< BOA SORTE! >":}', f'-=' * 5)
