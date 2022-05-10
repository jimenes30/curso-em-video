# Matriz em Python
print(f'{" Matriz em Python ":-^60}')
lista = [[], [], []]
for c in range(0, 3):
    lista[0].append(int(input(f'Digite um valor para [0][{c}]: ')))
    lista[1].append(int(input(f'Digite um valor para [1][{c}]: ')))
    lista[2].append(int(input(f'Digite um valor para [2][{c}]: ')))
print("-" * 60)
print(f'{" ":<15}', f'[ {lista[0][0]:^5} ][ {lista[0][1]:^5} ][ {lista[0][2]:^5} ]')
print(f'{" ":<15}', f'[ {lista[1][0]:^5} ][ {lista[1][1]:^5} ][ {lista[1][2]:^5} ]')
print(f'{" ":<15}', f'[ {lista[2][0]:^5} ][ {lista[2][1]:^5} ][ {lista[2][2]:^5} ]')
print("-" * 60)
