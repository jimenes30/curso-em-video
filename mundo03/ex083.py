# Validando expressões matemáticas
expr = str(input("Digite sua expressão: "))
# expr = str("((a+b)*c)(x+y(3+2/3)*z)")
pilha = []
for simb in expr:               # Para cada simbolo na expressão verifique
    if simb == "(":             # Se o símbolo é um "("
        pilha.append("(")       # Se for adicione "(" na temp pilha
    elif simb == ")":           # Se não se o simbolo for um "("
        if len(pilha) > 0:      # Se a pilha possui algum elemento
            pilha.pop()         # Apague o último elemento
        else:                   # Se não
            pilha.append(")")   # Adicione ")" na temp pilha
if len(pilha) > 0:
    print(f'\033[31mExpressão Inválida!')
else:
    print(f'\033[32mExpressão Válida!')
