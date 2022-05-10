# Funcionalidades Monetárias

def metade(preço):
    res = float(preço)
    res *= 0.5
    return res


def dobro(preço):
    res = float(preço)
    res *= 2
    return res


def aumentar(preço, taxa=10):
    res = float(preço)
    res *= (1 + (taxa/100))
    return res


def diminuir(preço, taxa=10):
    res = float(preço)
    res *= (1 - (taxa/100))
    return res
