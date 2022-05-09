# Verificando as primeiras letras de um texto
cidade = input('Em que cidade você nasceu ?\n').strip()
print(cidade[:5].upper() == 'SANTO')
if cidade.upper()[:5] == 'SANTO':
    print('Começa com santo')
else:
    print('Não começa com santo')
