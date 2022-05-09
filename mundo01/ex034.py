# Aumentos múltiplos
salário = float(input('Qual o salário do funcionário ? R$ '))
novo_salário = salário * 1.15
aumento = 15
if salário > 1250:
    novo_salário = salário * 1.1
    aumento = 10
print('Quem ganhava R$ {:.2f}, ganhará um aumento'
      ' de {}%, e seu novo salário será R$ {:.2f}'.format(salário, aumento, novo_salário))
