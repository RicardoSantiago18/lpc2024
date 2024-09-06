import random

caminho = 'Caminho do arquivo.txt' 

with open(caminho, 'r') as arquivo:
    palavras = arquivo.readlines()

palavra_escolhida = random.choice(palavras).strip()
palavra_secreta = ['_' for i in palavra_escolhida]


def jogo_da_forca():
    tentativas = 6
    erros = []
    acertos = []

    while len(erros) < tentativas and '_' in palavra_secreta:
        print(f'Palavra: {''.join(palavra_secreta)}')
        print(f'Palpites errados: {", ".join(erros)}')

        letra = input('Digite uma letra: ').lower()

        if letra in acertos or letra in erros:
            print('Você já tentou essa letra. Tente outra.')
            continue

        if letra in palavra_escolhida:
            acertos.append(letra)
            for i in range(len(palavra_escolhida)):
                if palavra_escolhida[i] == letra:
                    palavra_secreta[i] = letra
        else:
            erros.append(letra)
            print(f'Letra errada! Você tem {tentativas - len(erros)} tentativas restantes.')

    if '_' not in palavra_secreta:
        print(f'Parabéns, você venceu! a palavra era: {palavra_escolhida}')
    else:
        print(f'Você perdeu! A palavra era: {palavra_escolhida}')


jogo_da_forca()
