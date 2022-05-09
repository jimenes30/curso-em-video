# Alistamento Militar
import datetime
print('Digite seu sexo.')
sexo = str(input('[ F ] para FEMININO\n[ M ] para MASCULINO\nSua resposta: ')).strip().upper()
if sexo[0] == 'M':
    ano_nascimento = int(input('Ano de nascimento:\n'))
    ano_atual = datetime.date.today().year
    ano_alistamento = ano_nascimento + 18
    idade = ano_atual - ano_nascimento
    print('Quem nasceu em {} tem {} anos em {}.'.format(ano_nascimento, idade, ano_atual))
    if idade < 18:
        print('Ainda faltam {} anos para seu alistamento.\n'
              'Seu alistamento será em {}.'.format(18 - idade, ano_alistamento))
    elif idade > 18:
        print('Você já deveria ter se alistado há {} anos.\n'
              'Seu alistamento foi em {}.'.format(idade - 18, ano_alistamento))
    elif idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE')
elif sexo[0] == 'F':
    print('Você não precisa se alistar.')
else:
    print('Opção Inválida')
