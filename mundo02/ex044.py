# Gerenciador de Pagamentos
print(f'{" Lojas Alfredo ":=^33}')
valor = float(input('Preço das compras: R$ '))
opção = 0
print('FORMAS DE PAGAMENTO\n[ 1 ] à vista Dinheiro/Cheque\n[ 2 ] '
      'à vista no Cartão\n[ 3 ] 2x no Cartão\n[ 4 ] 3x ou mais no Cartão')
while opção not in range(1, 5):
    opção = int(input('Qual é a opção ?\n'))
    if opção == 1:
        print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} à vista'.format(valor, valor * 0.9))
    elif opção == 2:
        print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} à vista no cartão'.format(valor, valor * 0.95))
    elif opção == 3:
        print('Sua compra de R$ {:.2f} vai custar o valor formal parcelado de 2x SEM JUROS'.format(valor))
    elif opção == 4:
        parcelas = int(input('Quantas parcelas ? '))
        novo_valor = valor * 1.2
        valor_parcelas = novo_valor / parcelas
        print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS.'
              '\nSua compra de R$ {:.2f} vai custar R$ {:.2f} no final'
              .format(parcelas, valor_parcelas, valor, novo_valor))
    else:
        print('Opção Inválida. Tente novamente')
