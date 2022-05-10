# Funcionalidades Monetárias

def moeda(preço=0, cifra='R$'):
    r = f'{cifra}{preço:.2f}'.replace(".", ",")
    return r


def metade(preço=0):
    res = float(preço)
    res *= 0.5
    return res


def dobro(preço=0):
    res = float(preço)
    res *= 2
    return res


def aumentar(preço=0, taxa=10):
    res = float(preço)
    res *= (1 + (taxa/100))
    return res


def diminuir(preço=0, taxa=10):
    res = float(preço)
    res *= (1 - (taxa/100))
    return res
