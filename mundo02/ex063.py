# Sequência de Fibonacci v1.0
print('{:-^45}'.format(' Sequência de Fibonacci v1.0 '))
limite = int(input('Quantos termos você quer mostrar?  '))
print('Os {} primeiros termos da Sequência de Fibonacci são:'.format(limite))
contador = 0
anterior_distante = 0
anterior_próximo = 1
while contador != limite:
    contador += 1
    próximo = anterior_distante + anterior_próximo
    print('{}'.format(anterior_distante), end=' → ')
    anterior_distante = anterior_próximo
    anterior_próximo = próximo
print('FIM')
