# Função de Contador
from time import sleep


def contador(inicio, fim, passo):
    print(f'-=' * 20)
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio >= fim:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ', flush=True)
            cont -= passo
            sleep(0.1)
    else:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end=' ', flush=True)
            cont += passo
            sleep(0.1)
    print(f'FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print(f'-=' * 20)
print(f'Agora é sua vez de personalizar a contagem !')
contador(int(input("Início: ")), int(input("Fim:    ")), int(input("Passo:  ")))
