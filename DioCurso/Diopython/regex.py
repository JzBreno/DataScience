import re


def validar_numero(numero):
    padrao = r"\(\d{2}\) 9\d{4}-\d{4}"
    if re.fullmatch(padrao, numero):
        return True
    else:
        return False


teste = validar_numero(input())
if teste:
    print('Número de telefone válido.')
else:
    print('Número de telefone inválido.')


