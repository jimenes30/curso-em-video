# Aquele clássico da media
nota1 = float(input('Primeira nota:\n'))
nota2 = float(input('Segunda nota:\n'))
média = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a media do aluno será {:.1f}'.format(nota1, nota2, média))
if média < 5:
    print('o aluno está \033[31mREPROVADO!!!\033[m')
elif 6.9 > média > 5:
    print('o aluno está de \033[33mRECUPERAÇÃO\033[m')
elif média >= 7:
    print('o aluno está \033[34mAPROVADO!\033[m')
