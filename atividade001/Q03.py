cpf = input("Informe o CPF do usuário: ").strip()


def verificar_formatacao(cpf):
    if len(cpf) != 14:
        return False

    if cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
        return False

    return True


digito_verificador1 = int(cpf[12])
digito_verificador2 = int(cpf[13])


def validar_digito1(cpf):
    soma = 0
    cpf = cpf.replace('.', '').replace('-', '')
    for i in range(len(cpf) - 2):
        produto = int(cpf[i]) * (10 - i)
        soma += produto
    resto = soma % 11
    if resto < 2:
        resultado = 0
    else:
        resultado = 11 - resto

    return resultado == digito_verificador1


def validar_digito2(cpf):
    soma = 0
    cpf = cpf.replace('.', '').replace('-', '')
    for i in range(len(cpf) - 1):
        produto = int(cpf[i]) * (11 - i)
        soma += produto
    resto = soma % 11
    if resto < 2:
        resultado = 0
    else:
        resultado = 11 - resto

    return resultado == digito_verificador2


def main():
    if not verificar_formatacao(cpf):
        print("Formatação Inválida")

    if validar_digito1(cpf) and validar_digito2(cpf):
        print("CPF Válido")
    else:
        print("CPF Inválido")


if __name__ == '__main__':
    main()
