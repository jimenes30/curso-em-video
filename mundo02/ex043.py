# Índice de Massa Corporal
print('{:=^30}'.format('Cálculo de IMC'))
peso = float(input('Qual é seu Peso ? (em kg): '))
altura = float(input('Qual é sua altura ? (em cm): ')) / 100
imc = peso / (altura ** 2)
print('O seu IMC é de {:.1f}'.format(imc))
if 0 < imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.6 < imc < 24.9:
    print('PARABÉNS! Você está na faixa de PESO NORMAL')
elif 25 < imc < 29.9:
    print('Você está em SOBREPESO')
elif 30 < imc < 34.9:
    print('Você está em OBESIDADE')
elif 35 < imc < 39.9:
    print('Você está em OBESIDADE SEVERA')
elif imc > 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado !')
