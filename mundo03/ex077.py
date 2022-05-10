# Contando vogais em Tuplas
palavras = ['aprender', 'programar', 'linguagem',
            'python', 'curso', 'gratis', 'estudar',
            'praticar', 'trabalhar', 'mercado', 'programador', 'futuro']
print(f'{" Contando vogais em Tuplas ":-^50}')
"""
# Meu método
for palavra in range(0, len(palavras)):
    print(f'Na palavra {palavras[palavra]} temos {"a " * palavras[palavra].count("a")}{"e " * palavras[palavra].count("e")}'
          f'{"palavra " * palavras[palavra].count("palavra")}{"o " * palavras[palavra].count("o")}{"u " * palavras[palavra].count("u")}', end='\n')
"""
# método comum
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')
