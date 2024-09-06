import random

valores = []

def lançamento():
    valor = random.randint(1, 6)
    return valor


while len(valores) < 100:
    valores.append(lançamento())

print(f'\nResultado geral dos rolamentos do dado: {valores}\n')

for lado in range(1, 7):
    qtd = valores.count(lado)
    print(f'O lado {lado} apareceu {qtd} vezes')
