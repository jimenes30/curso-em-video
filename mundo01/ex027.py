# Primeiro e Último nome de uma pessoa
nome_completo = str(input('Digite seu nome completo:\n')).title().strip()
nome_fatiado = nome_completo.split()
print('Prazer em te conhecer !')
print('Seu primeiro nome é {}'.format(nome_fatiado[0]))
print('Seu último nome é {}'.format(nome_fatiado[-1]))
