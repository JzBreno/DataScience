
variavel  = 100


def aplicar_aumento(variavel):
    if variavel == 100:
        return int(variavel * 0.2) + variavel
    
print(aplicar_aumento(variavel))