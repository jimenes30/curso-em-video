# Conversor de bases numéricas
número = int(input('Digite um número inteiro qualquer:\n'))
print('Escolha uma das bases para conversão:')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para {} é igual a {}'.format(número, 'BINÁRIO', bin(número)[2:]))
elif opção == 2:
    print('{} convertido para {} é igual a {}'.format(número, 'OCTAL', oct(número)[2:]))
elif opção == 3:
    print('{} convertido para {} é igual a {}'.format(número, 'HEXADECIMAL', hex(número)[2:]))
else:
    print('opção inválida')
