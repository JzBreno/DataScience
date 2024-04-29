var = map(int, input('digite').split())

a, b = var


def aplicar_aumento(a, b):
    return int(a+(a*((b/100))))


print(aplicar_aumento(a, b))
