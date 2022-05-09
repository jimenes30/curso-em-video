# Validação de pessoas
sexo = '#'
while sexo[0] not in 'FfMm':
    print('-' * 30)
    sexo = str(input('\nSexo [M/F]: ')).strip().upper()
    if sexo == '' or sexo[0] not in 'FfMm':
        sexo = '#'
        print('Opção Inválida. Tente Novamente.\n')
if sexo[0] == 'M':
    print('=' * 30)
    print('Sexo MASCULINO \033[34m♂\033[m salvo')
    print('=' * 30)
elif sexo[0] == 'F':
    print('=' * 30)
    print('Sexo FEMININO \033[31m♀\033[m salvo')
    print('=' * 30)
