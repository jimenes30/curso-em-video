# Tratando vários valores v1.0
print('{:-^50}'.format(' Tratando Valores v1.0 '))
num = soma = contador = 0
while num != 999:
    contador += 1
    num = int(input('Digite um número inteiro [999 p/ parar]: '))
    if num != 999:
        soma += num
    else:
        contador -= 1
print('Você digitou {} números, e a soma foi {}'.format(contador, soma))
