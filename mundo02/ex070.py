# Estatísticas em produtos
print('~' * 50)
print(f'{"LOJÃO SUPER BARATÃO":-^50}')
print('~' * 50)
total = mais_de_mil = mais_barato = contador = 0
nome_produto = '0'
while True:
    contador += 1
    nome = str(input('Nome do Produto: '))
    preço = float(input('Valor: '))
    if contador == 1 or preço < mais_barato:
        mais_barato = preço
        nome_produto = nome
    if preço > 1000:
        mais_de_mil += 1
    total += preço
    escolha = '0'
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print(f'{"FIM DO PROGRAMA":-^50}')
print(f'Total a pagar: R$ {total:.2f}')
print(f'Produtos que custam mais de mil reais: {mais_de_mil}')
print(f'O produto mais barato foi {nome_produto}, custou apenas R$ {mais_barato:.2f}')
