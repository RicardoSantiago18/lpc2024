num = int(input('Informe um número inteiro em um intervalo de 0 à 99: '))

unidades = ['zero' ,'um', 'dois', 'três', 'quatro', 'cinco',
            'seis', 'sete', 'oito', 'nove']

dezenas = ['', '', 'vinte', 'trinta', 'quarenta', 'cinquenta',
           'sessenta', 'setenta', 'oitenta', 'noventa']

diferenciais = ['dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze',
                'dezesseis', 'dezessete', 'dezoito', 'dezenove']

def numero_extenso(num):
    if 0 <= num < 10:
        return unidades[num]

    elif 10 <= num < 20:
        return diferenciais[num - 10]

    if 20 <= num < 100:
        dezena = num // 10
        unidade = num % 10
        if unidade == 0:
            return dezenas[dezena]
        else:
            return f"{dezenas[dezena]} e {unidades[unidade]}"
    else:
        return "fora do intervalo permitido"

print(numero_extenso(num))
