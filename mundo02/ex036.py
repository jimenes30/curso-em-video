# Aprovando Empréstimo
print('\033[30m-\033[m\033[37m=\033[m' * 22)
print('{:^51}'.format('\033[4mAnálise de Empréstimo Simples\033[m'))
print('\033[30m-\033[m\033[37m=\033[m' * 22)
casa = float(input('Digite o valor da casa:\nR$ '))
salário = float(input('Digite o salário do comprador:\nR$ '))
anos = int(input('Quantos anos de financiamento ?\n'))
prestação = casa / (anos * 12)
situação = '\033[1;33mAprovado\033[m'
if prestação > salário * 0.3:
    situação = '\033[31mReprovado\033[m'
print('Para pagar uma casa de R$ {:.2f} em {} anos, a prestação deve ser de '
      'R$ \033[4m{:.2f}\033[m ao mês.\nEmpréstimo {}!'.format(casa, anos, prestação, situação))
