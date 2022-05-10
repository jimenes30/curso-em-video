# Funcionalidades Monetárias

def moeda(preço=0, cifra='R$'):
    res = f'{cifra}{preço:.2f}'.replace(".", ",")
    return res


def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def aumentar(preço=0, taxa=10, formato=False):
    res = preço * (1 + (taxa/100))
    return res if not formato else moeda(res)


def diminuir(preço=0, taxa=10, formato=False):
    res = preço * (1 - (taxa/100))
    return res if not formato else moeda(res)
