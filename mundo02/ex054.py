# Grupo da maioridade
from datetime import date
maiores = 0
menores = 0
idade = 0
ano_atual = date.today().year
for i in range(1, 8):
    ano_nascimento = int(input('Digite o ano de nascimento da {}° Pessoa: '.format(i)))
    idade = ano_atual - ano_nascimento
    if idade >= 21:
        maiores += 1
    elif idade < 21:
        menores += 1
print('Ao todo {} pessoas são \033[32mMAIORES DE IDADE\033[m. '
      'E {} ainda são \033[33mMENORES DE IDADE\033[m'.format(maiores, menores))

