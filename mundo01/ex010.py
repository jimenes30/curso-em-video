# Conversor de moedas
r = float(input('Quanto dinheiro você tem na carteira ? R$ '))
d = r * 0.17823088
e = r * 0.15113274
print('Com R${} você pode comprar US${:.2f} ou €{:.2f}'.format(r, d, e))
