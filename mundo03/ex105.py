# Analisando e gerando dicionários
maior = menor = 0


def notas(*dados, sit=False):
    """
        --> Função para calcular a quantidade de notas, maior nota, menor note, média e situação(opcional)
    :param dados: notas a serem calculadas
    :param sit: (opicional) mostra a situação referente a média
    :return: Retorna um dicionário com as variáveis total, maior, menor, média, situação
    """
    global maior, menor
    boletim = {"total": len(dados)}
    for i in range(0, len(dados)):
        if i == 0:
            maior = menor = dados[i]
        else:
            if dados[i] > maior:
                maior = dados[i]
            if dados[i] < menor:
                menor = dados[i]
    média = sum(dados) / len(dados)
    boletim["maior"] = maior
    boletim["menor"] = menor
    boletim["média"] = média
    if sit:
        if 10 >= média > 7:
            boletim["situação"] = 'Excelente'
        elif 6 >= média > 5:
            boletim["situação"] = 'Bom'
        elif 5 > média >= 0:
            boletim["situação"] = 'Ruim'
    return boletim


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
