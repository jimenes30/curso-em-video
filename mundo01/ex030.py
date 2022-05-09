# Par ou ímpar
numero = int(input('\033[37mMe diga um número qualquer:\033[m\n'))
if numero % 2 == 0:
    print('O número {} é \033[34mPAR\033[m !'.format(numero))
else:
    print('O número {} é \033[31mÌMPAR\033[m !'.format(numero))
