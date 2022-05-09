# Custo da viagem
distância = float(input('Qual a distância da sua viagem ? (em km)\n'))
valorDaPassagem = distância * 0.5
if distância > 200:
    valorDaPassagem = distância * 0.45
print('Você está prestes a começar uma viagem de {}km'.format(distância))
print('E o preço da sua passagem será de R$ {:.2f}'.format(valorDaPassagem))
