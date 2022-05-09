# Criando um menu de opções
from time import sleep
print('{:¨^40}'.format(' Lógica de Menu [⌂] '))
valor1 = int(input('Digite um número: '))
valor2 = int(input('Digite um número: '))
escolha = ''
while escolha != '5':
    print('\n{:-^40}'.format(' Menu de opções '))
    print("""
    [ 1 ] Soma de 2 valores
    [ 2 ] Multiplicação de 2 valores
    [ 3 ] Maior de 2 valores
    [ 4 ] Digitar novamente os números
    [ 5 ] Sair\n""")
    escolha = str(input('Sua opção: '))
    if escolha == '1':
        print('você escolheu a opção 1')
        print('{} + {} = {}'.format(valor1, valor2, valor1 + valor2))
        for i in range(0, 5):
            print('•', end='    ')
            sleep(1)
    elif escolha == '2':
        print('Você escolheu a opção 2')
        print('{} x {} = {}'.format(valor1, valor2, valor1 * valor2))
        for i in range(0, 5):
            print('×', end='    ')
            sleep(1)
    elif escolha == '3':
        print('Você escolheu a opção 3')
        sleep(0.2)
        if valor1 > valor2:
            print('O maior valor é {}.\nConsequentemente o menor será {}'.format(valor1, valor2))
        elif valor1 < valor2:
            print('O maior valor é {}.\nConsequentemente o menor valor será {}'.format(valor2, valor1))
        else:
            print('Os valores são IGUAIS. NÃO HÁ MAIORES ou MENORES')
        for i in range(0, 5):
            print('☼', end=' ')
            sleep(1)
    elif escolha == '4':
        print('Você escolheu a opção 4')
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor:'))
    elif escolha == '5':
        print('')
    else:
        print('Opção Inválida. Tente Novamente')
print('fim do programa')
