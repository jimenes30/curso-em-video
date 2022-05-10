# Cadastro de Trabalhador em Python
from datetime import datetime
dados = {"nome": str(input("Nome: "))}
ano_nasc = int(input("Ano de Nascimento: "))
CTPS: int = int(input("Carteira de Trabalho (0 não tem): "))
dados["idade"] = datetime.now().year - ano_nasc
dados["CTPS"] = CTPS
if CTPS != 0:
    dados["contratação"] = int(input("Ano de Contratação: "))
    dados["salário"] = float(input("Salário: R$ "))
    dados["aposentadoria"] = (dados["contratação"] + 35) - ano_nasc
print(f'-=' * 30)
for k, v in dados.items():
    print(f'    - {k} tem o valor {v}')
