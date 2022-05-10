# Dicionário em Python
dados = {"Nome": str(input("Nome: "))}
dados["Média"] = float(input(f'Media de {dados["Nome"]}: '))
if 5 < dados["Média"] < 7:
    dados["Situação"] = "Recuperação"
elif 0 <= dados["Média"] < 5:
    dados["Situação"] = "Reprovado!"
elif 10 >= dados["Média"] > 7:
    dados["Situação"] = "Aprovado"
else:
    print('Média inválida. Digite uma média entre 0 e 10')
print("-=" * 20)
for k, v in dados.items():
    print(f'    - {k} é {v}')
