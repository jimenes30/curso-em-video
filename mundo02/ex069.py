# Análise de pessoas do grupo
maior18 = 0
homens = 0
mulheres20 = 0
while True:
    sexo = escolha = '0'
    print('_' * 40)
    print(f'{"CADASTRE UMA PESSOA":^40}')
    print('_' * 40)
    idade = int(input('Idade: '))
    if idade > 18:
        maior18 += 1
    while sexo[0] not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        homens += 1
    elif sexo == 'F':
        if idade < 20:
            mulheres20 += 1
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar ? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print(f'Pesssoas com mais de 18 anos  : {maior18}')
print(f'Homens cadastrados            : {homens}')
print(f'Mulheres com menos de 20 anos : {mulheres20}')
