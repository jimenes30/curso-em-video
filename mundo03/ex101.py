# Funções para votação


def voto(ano_nascimento):
    from datetime import datetime
    idade = datetime.today().year - ano_nascimento
    if idade >= 65 or 18 > idade >= 16:
        return f'Com {idade} anos: VOTO OPCIONAL'
    elif idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


# Programa Principal
print(f'-' * 40)
ano = int(input("Em que ano você nasceu ? "))
print(voto(ano))
