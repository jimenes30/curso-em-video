# Aluguel de carros
dias = int(input('Quantos dias alugado ?\n'))
km = float(input('Quantos km rodados ?\n'))
conta = (60 * dias) + (0.15 * km)
print('O total a pagar é R$ {:.2f}'.format(conta))
# R$ 60.00 por dia R$ 0.15 por km rodado
