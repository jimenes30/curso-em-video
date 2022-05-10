# Lista ordenada sem repetições
print(f'{"Lista Crescente SEM SORTED":_^50}')
lista = []
for c in range(0, 5):
    n = int(input("Digite um valor: "))
    # Se for primeiro ou o último
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print(f'Adicionado ao final da temp !')
    # Se for no meio
    else:
        pos = 0
        while True:
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Valor {n} adicionoado na posição {pos}')
                break
            pos += 1
print(f'Você digitou os valores {lista}')
