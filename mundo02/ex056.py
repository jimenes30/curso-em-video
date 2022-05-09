# Analisador Completo
#from datetime import date
#ano_atual = date.today().year
print('{:-^50}'.format(' Analisador Completo '))
pessoas = int(input('Quantas pessoas analisar ? '))
soma = 0
maior_idade = 0
mulheres_menores_20 = 0
homem_mais_velho = ''
for i in range(1, pessoas + 1):
    print('{} {}° Pessoa {}'.format('-' * 10, i, '-' * 10))
    nome = str(input('Nome: ')).strip().upper()
    # ano_nascimento = int(input('Digite o ano de nascimento da {}° Pessoa:\p'.format(palavra)))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [ M/F ]: '.format(i))).strip().upper()
    # idade = ano_atual - ano_nascimento
    soma += idade
    if idade > maior_idade and sexo in 'Mm':
        maior_idade = idade
        homem_mais_velho = nome
    if idade < 20 and sexo[0 == 'F']:
        mulheres_menores_20 += 1
média = soma / pessoas
print('A media de idade do grupo foi: {:.1f} anos'.format(média))
print('O homem mais velho é: {} com {} anos'.format(homem_mais_velho, maior_idade))
print('Quantidade de mulheres menores de 20 anos: {}'.format(mulheres_menores_20))
