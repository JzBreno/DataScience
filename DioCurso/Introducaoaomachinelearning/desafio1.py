lista = []
pos = 0
neg = 0


def somavalor(numero, pos, neg):
    if numero > 0:
        pos += 1
    if numero < 0:
        neg += 1
    return pos, neg


def validador(numero, pos, neg):
    if numero > 0:
        print('positivo!')
        return somavalor(numero, pos, neg)
    elif numero < 0:
        print('negativo!')
        return somavalor(numero, pos, neg)
    else:
        print(pos, f'números positivos,', neg, 'números negativos')
        return somavalor(numero, pos, neg)


while True:
    numero = int(input())
    if numero == 0:
        pos, neg = validador(numero, pos, neg)
        break
    else:
        lista.append(numero)
        pos, neg = validador(numero, pos, neg)
