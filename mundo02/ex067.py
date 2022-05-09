# Tabuada v3.0
print(f'{" Tabuada v3.0 ":-^70}\n')
contador = 0
while True:
    print('Gostaria de ver a tabuada de qual número ? [negativo p/ nenhum]')
    número = int(input('Digite um número: '))
    if número < 0:
        break
    for contador in range(1, 11):
        print(f'{número:>2} x {contador:>2} = {número * contador:>2}')
    print(f'{"↔":-^60}\n')
print('-' * 50)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre !')
print('-' * 50)
