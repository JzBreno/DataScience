import defscalc
import random

soma = ['somar', 'adicionar','+']
subtrai = ['diminuir', '-', 'subtrair']
multiplicar = ['multiplica', 'multiplicar', '*','x', 'vezes']
dividir = ['dividir', '/']

todos = ['somar', 'adicionar','+','diminuir', '-', 'subtrair',  'multiplica', 'multiplicar', '*','x', 'vezes','dividir', '/' ]


for i in range(10):
    a = int(random.randint(1, 10))
    b = int(random.randint(1, 10))
    n = str(random.choice(todos))
    print(n)
    print(defscalc.calculadora(n)(a,b))