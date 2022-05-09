# Analisando triângulo
print('\033[33m-=\033[m' * 25)
print('{:^50}'.format('Analisador de Triângulos'))
print('\033[36m-=\033[m' * 25)
a = float(input('Digite a reta a:\n'))
b = float(input('Digite a reta b:\n'))
c = float(input('Digite a reta c:\n'))
if a < (b + c) and b < (a + b) and c < (a + b):
    print('Os segmentos acima \033[34mPODEM FORMAR\033[m um triângulo!')
else:
    print('Os segmentos acima \033[31mNÃO\033[m PODEM FORMAR um triângulo!')
