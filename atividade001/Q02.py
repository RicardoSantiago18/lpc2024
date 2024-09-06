frase = str(input("Digite uma frase: ")).strip().upper()
frase = frase.replace(" ", "")

if frase == frase[::-1]:
    print('A frase digitada é um palíndromo')

else:
    print('A frase digitada não é um palíndromo')

print(frase)
print(frase[::-1])