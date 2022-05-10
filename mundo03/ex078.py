# Maior e Menor valores na temp
valores = [int(input('Digite um valor para a posição 0: ')), int(input('Digite um valor para a posição 1: ')),
           int(input('Digite um valor para a posição 2: ')), int(input('Digite um valor para a posição 3: ')),
           int(input('Digite um valor para a posição 4: '))]
maior = max(valores)
menor = min(valores)
posição_maior = []
posição_menor = []
for posição in range(0, len(valores)):
    print(f'Valor {valores[posição]}, na posição {posição}')
    if valores[posição] == maior:
        posição_maior.append(posição)
    if valores[posição] == menor:
        posição_menor.append(posição)
print('-=' * 30)
print(f'Você digitou os valores {valores}')
if maior == menor:
    print('Você digitou valores iguais, temos uma temp homogênea')
else:
    print(f'O maior valor foi {maior}, na posição {posição_maior}')
    print(f'O menor valor foi {menor}, na posição {posição_menor}')
print(f'{"Fim do Programa":-^60}')
