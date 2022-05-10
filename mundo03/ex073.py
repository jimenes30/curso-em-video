# Tuplas com time de futebol
brasileirão_2019 = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico Paranaense', 'São Paulo',
                    'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético - MG',
                    'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print(f'{" Tabela Brasileirão 2019 ":-^50}')
print('Os 5 primeiros colocados do Brasileirão 2019 foram: ')
for posição in range(0, 5):
    print(f'{posição + 1:>2}° - {brasileirão_2019[posição]}')
print('-=' * 45)
print('Os últimos 4 colocados do ranking foram: ')
for posição in range(-4, 0):
    print(f'{len(brasileirão_2019)+ 1 + posição:>2}° - {brasileirão_2019[posição]}')
print('-=' * 45)
print('Times em ordem alfabética:')
for posição in range(0, len(brasileirão_2019)):
    print(f'{posição + 1:>2}° - {sorted(brasileirão_2019)[posição]}')
print('-=' * 45)
print(f'Posição do Chapecoense no campeonato: {brasileirão_2019.index("Chapecoense") + 1}ª Posição')
