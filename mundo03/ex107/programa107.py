# Programa principal
from moeda import aumentar, diminuir, dobro, metade
n = str(input("Digite o Preço: R$ "))
print(f'O dobro de R$ {n} é R$ {dobro(n):.2f}')
print(f'A metade de R$ {n} é R$ {metade(n):.2f}')
print(f'Aumentando 10% temos R$ {aumentar(n):.2f}')
print(f'Diminuindo 10% temos R$ {diminuir(n):.2f}')
