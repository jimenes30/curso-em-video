# Classificando atletas
import datetime
ano_nascimento = int(input('Ano de nascimento:\n'))
ano_atual = datetime.date.today().year
idade = ano_atual - ano_nascimento
classe = 'MASTER'
if 0 < idade <= 9:
    classe = 'MIRIM'
elif 9 < idade <= 14:
    classe = 'INFANTIL'
elif 14 < idade <= 19:
    classe = 'JÚNIOR'
elif 19 < idade <= 25:
    classe = 'SÊNIOR'
print('O atleta tem {} anos.\nClassificação: {}.'.format(idade, classe))
