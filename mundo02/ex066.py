# Vários números com flag
print(f'{" [Teste do Break] ":=^50}')
contador = soma = 0
while True:
    número = int(input('Digite um número inteiro (999 p/ parar): '))
    if número == 999:
        break
    contador += 1
    soma += número
print(f'Você digitou {contador} números e a soma vale {soma}')
