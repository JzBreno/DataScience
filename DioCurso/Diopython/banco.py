import os
from time import sleep
extratosaque = []
limitesaques = 3
saldo = float()
limitediario = 500
deposito = float()
saque = float()

print("Bem vindo ao banco")

while True:
    menu = int(input("""
[1] - Saldo
[2] - Depósitar
[3] - Extrato
[4] - Sacar
[5] - Sair
"""))

    if menu > 0 and 6 > menu:
        match menu:
            case 1:
                print(f'Seu saldo é:', saldo)
            case 2:
                deposito = int(input("Digite o valor que irá Depositar: "))
                saldo += deposito
            case 3:
                if len(extratosaque) == 0:
                    print("Sem Saques feitos")
                else:
                    print("Seu Extrato é: ")
                    for i in extratosaque:
                        print(i, f'Reais')
            case 4:
                print("Seu limite diario é 500 Reais")
                print(f'Seu limite de saques diarios atualmnete são', limitesaques)
                saque = int(input("Digite o valor que deseja sacar: "))
                if saque <= 500 and limitesaques > 0 and saldo > 0:
                    limitesaques -= 1
                    extratosaque.append(saque)
                    saldo -= saque
                    print("Saque Feito com Sucesso!")
                else:
                    if saldo == 0:
                        print('Seu saldo está Zerado!')
                    if limitesaques == 0:
                        print('Seu milite de saques diarios está Zerado!')
                    if saque > 500:
                        print('Seu limite de saque diario é apenas de 500 Reais')

    else:
        print("DIGITE UM NUMERO QUE TENHA FUNCIONALIDADE")
    sleep(3)
    os.system("cls")
