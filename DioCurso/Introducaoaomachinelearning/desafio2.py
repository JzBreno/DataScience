"""
Seu objetivo é criar um modelo de machine learning capaz de classificar frutas com base em três características:
 peso, textura (suave ou áspera) e cor (vermelha, laranja ou amarela).
 Cada tipo de fruta tem limites específicos para essas características.
Maçã:

Peso mínimo: 130 gramas
Textura: Ápera (rough)
Cor: Vermelha (red)
Laranja:

Peso mínimo: 120 gramas
Textura: Suave (smooth)
Cor: Laranja (orange)
Morango:

Peso mínimo: 150 gramas
Textura: Suave (smooth)
Cor: Vermelha (red)
Banana:

Peso mínimo: 150 gramas
Textura: Áspera (rough)
Cor: Amarela (yellow)
Entrada
Seu código deve receber as seguintes entradas do usuário:

Peso da fruta (em gramas): um número real que representa o peso da fruta.
Textura da fruta (suave ou áspera): uma string indicando se a fruta é suave ("smooth") ou áspera ("rough").
Cor da fruta (vermelha, laranja ou amarela): uma string indicando a cor da fruta.
Saída
O código deve produzir uma saída indicando a classificação da fruta com base nas características fornecidas.
"""

peso = float(input())
textura = input()
cor = input()


def classificar(peso, textura, cor):
    if peso >= 130 and textura == 'rough' and cor == 'red':
        return 'A fruta é um macã!'
    elif peso >= 120 and textura == 'smooth' and peso == 'orange':
        return 'A fruta é um Laranja!'
    elif peso >= 150 and textura == 'smooth' and cor == 'red':
        return 'A fruta é um Morango!'
    elif peso >= 150 and textura == 'rough' and cor == 'yellow':
        return 'A fruta é um Banana!'
    else:
        return 'Não foi possível classificar a fruta.'


msg = classificar(peso, textura, cor)
print(msg)

peso = float(input())
textura = input()
cor = input()

mulher 
def classificar(peso, textura, cor):
    if peso >= 130 and textura == 'rough' and cor == 'red':
        return 'A fruta é um macã!'
    elif peso >= 120 and textura == 'smooth' and peso == 'orange':
        return 'A fruta é um Laranja!'
    elif peso >= 150 and textura == 'smooth' and cor == 'red':
        return 'A fruta é um Morango!'
    elif peso >= 150 and textura == 'rough' and cor == 'yellow':
        return 'A fruta é um Banana!'
    else:
        return 'Não foi possível classificar a fruta.'


msg = classificar(peso, textura, cor)
print(msg)