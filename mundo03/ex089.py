# Boletim com listas compostas
temp = []
nomes = []
nota1 = []
nota2 = []
boletim = []
medias = []
while True:
    nomes.append(str(input("Nome: ")))
    temp.append(nomes[0])
    nota1.append(float(input("Nota1: ")))
    temp.append(nota1[0])
    nota2.append(float(input("Nota2: ")))
    temp.append(nota2[0])
    media = (nota1[0] + nota2[0]) / 2
    temp.append(media)
    nomes.clear()
    nota1.clear()
    nota2.clear()
    media *= 0
    boletim.append(temp[:])
    temp.clear()
    r = str(input("Quer continuar? [S/N] "))
    if r in "Nn":
        break
print(f'-=' * 15)
print(f'{"No.":<4}', f'{"Nome":<10}', f'{"   Média":>5}')
print(f'-' * 20)
for n in range(0, len(boletim)):
    print(f'{n:<4}', f'{boletim[n][0]:<10}', f'{boletim[n][3]:>5.1f}')
print(f'-' * 20)
while True:
    aluno = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if aluno == 999:
        break
    if aluno <= len(boletim) - 1:
        print(f'As notas de {boletim[aluno][0]} são {boletim[aluno][1:3]}')
        print(f'-' * 50)
    else:
        print(f'Opção inválida. Tente novamente !')
print(f'{"FINALIZANDO..."}', F'\n', f'<' * 4, F'{"VOLTE SEMPRE!":^10}', f'>' * 4)
