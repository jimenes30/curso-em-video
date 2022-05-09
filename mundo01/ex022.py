# Analisador de textos
"""Método 1"""
"""nome_completo = str(input('Digite seu nome completo: '))
nome_gordo = nome_completo.strip().split()
numero_de_nomes = len(nome_gordo)
letras = 0
for palavra in range(0, numero_de_nomes):
    letras += len(nome_gordo[palavra])
print('Analisando seu nome:')
print('Seu nome em MAIÚSCULAS é {}'.format(nome_completo.upper()))
print('Seu nome em minúsculas é {}'.format(nome_completo.lower()))
print('Seu nome tem ao todo {} letras'.format(letras))
print('Seu primeiro nome é {}, e ele tem {} letras'.format(nome_gordo[0], len(nome_gordo[0])))"""
"""Método 2"""
nome_completo = str(input('Digite seu nome completo: ')).strip()
nome_fatiado = nome_completo.split()
print('Analisando seu nome:')
print('Seu nome em maiúsculas é {}'.format(nome_completo.upper()))
print('Seu nome em minúsculas é {}'.format(nome_completo.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome_completo) - nome_completo.count(' ')))
print('Seu primeiro nome é {}, e ele tem {} letras'.format(nome_fatiado[0], len(nome_fatiado[0])))
