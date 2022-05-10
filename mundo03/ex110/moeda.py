# Funcionalidades Monetárias

def resumo(preço=0, aumento=0, redução=0):
    print(f'-' * 35)
    print(f'RESUMO DO VALOR'.center(35))
    print(f'-' * 35)
    print(f'Preço analisado:    \t{moeda(preço):<20}')
    print(f'Dobro do Preço:     \t{moeda(dobro(preço)):<20}')
    print(f'Metade do Preço:    \t{moeda(metade(preço)):<20}')
    print(f'{aumento}% de aumento:      \t{moeda(aumentar(preço, aumento)):<20}')
    print(f'{redução}% de redução:      \t{moeda(diminuir(preço, redução)):<20}')
    print(f'-' * 35)


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
