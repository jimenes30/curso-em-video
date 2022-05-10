# treino
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')
for palavra in palavras:
    print(f'Na palavra {palavra.upper()} temos: ', end='')
    if "a" in palavra:
        print(f'a ', end='')
    if "e" in palavra:
        print(f'e ', end='')
    if "i" in palavra:
        print(f'i ', end='')
    if "o" in palavra:
        print(f'o ', end='')
    if "u" in palavra:
        print(f'u ', end='')
    print('')
