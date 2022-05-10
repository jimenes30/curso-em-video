# Unindo dicionários e listas
dados = {}
pessoas = []
idade_lista = []
while True:
    dados["nome"] = str(input("Nome: "))
    while True:
        sexo = str(input("Sexo [M/F]: "))
        if sexo in "MmFf":
            dados["sexo"] = sexo
            break
        else:
            print(f'ERROR! por favor digite apenas M ou F.')
    dados["idade"] = int(input("Idade: "))
    idade_lista.append(dados["idade"])
    pessoas.append(dados.copy())
    while True:
        resposta = str(input("Quer continuar? [S/N]"))
        if resposta in "SsNn":
            break
        else:
            print(f'ERRO! Responda apenas S ou N')
    if resposta in "Nn":
        break
print(f'-=' * 30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
média = sum(idade_lista)/len(idade_lista)
print(f'B) A média de idade é de {média:.2f} anos.')
print(f'C) As mulheres cadastradas foram:', end=' ')
for e in pessoas:
    if e["sexo"] in "Ff":
        print(f'[{e["nome"]}]', end=' ')
print(f'\nD) Lista das pessoas que estão acima da média:')
for e in pessoas:
    if e["idade"] > média:
        print(f'    -> {e["nome"]}, {e["sexo"]}, {e["idade"]}')
print(f'-=' * 30)
print(f'\n{">> FINALIZADO <<":^50}')
