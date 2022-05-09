# Radar eletrônico
velocidade = float(input('Qual é a velocidade atual do carro ?\n'))
limite = 80
if velocidade > limite:
    multa = (velocidade - limite) * 7
    print('\033[31mMULTADO! Você excedeu o limite permitido que é de {}km/h\n'
          'Você deve pagar uma multa de R$ {:.2f}!\033[m'.format(limite, multa))
print('\033[32mTenha um bom dia! Dirija com segurança!\033[m')
