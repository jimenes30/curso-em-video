# Maior e menor valores
print('{:-^50}'.format(' Maior e Menor valores '))
maior = menor = contador = soma = escolha = 0
while escolha != 'N':
    contador += 1
    num = int(input('Digite um número inteiro: '))
    escolha = str(input('Continuar? [S/N]')).strip().upper()
    if escolha not in 'SsNn':
        print('Opção Inválida. Tente Novamente')
    soma += num
    if contador == 1:
        maior = menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
média = soma / contador
print('Você digitou {} números, e '.format(contador), end='')
print('a soma foi {}, e a media foi {:.2f}'.format(soma, média))
print('O maior valor foi {}, e o menor foi {}.'.format(maior, menor))
