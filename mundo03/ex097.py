# Um print especial
# def escreva(msg):
#    print(f'~' * len(msg) * 2)
#    print(f'{msg:^{len(msg) * 2}}')
#    print(f'~' * len(msg) * 2)
def escreva(msg):
    tam = len(msg) + 4
    print(f'~' * tam)
    print(f'  {msg}')
    print(f'~' * tam)


escreva("Olá, mundo!")
escreva("Curso em Vídeo")
escreva("CEV")
